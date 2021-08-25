import glob
import os
import argparse
from pathlib import Path
import random

def write_images(images,txt_file):
    '''
    Given a txt file and a list of image paths, writes the paths on the text
    Args:
        images (list): List of image paths
        txt_file (file object): a text file object where the image paths will be saved
    '''
    with open(txt_file,'w') as txt:
        txt.write("\n".join(str(image) for image in images))
    return None


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Custom splitter for data')
    parser.add_argument('--input', type = str, help='path to images')
    parser.add_argument('--split', type = float, default = 0.1, help='Split percentage, default is 0.1 (10% -> 80 train - 10 val - 10 test)')
    args = parser.parse_args()

    current_dir = Path(args.input) / "images"
    split = 0.1  # 10% validation set
    file_train = os.path.join(str(Path(args.input)),'train.txt')
    file_val = os.path.join(str(Path(args.input)),'val.txt')
    file_test = os.path.join(str(Path(args.input)),'test.txt')

    images = glob.glob(os.path.join(os.path.abspath(str(current_dir)),"*.jpg"))
    random.shuffle(images)
    train = images[:round((1-split)*len(images))]
    test = images[round((1-split)*len(images)):]
    val = train[round((1-split)*len(train)):]
    train = train[:round((1-split)*len(train))]
    [write_images(data[0],data[1]) for data in [[train,file_train],[val,file_val],[test,file_test]]]
