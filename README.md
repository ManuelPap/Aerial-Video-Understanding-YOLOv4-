
This is PyTorch implementation of [YOLOv4](https://github.com/WongKinYiu/PyTorch_YOLOv4)

## Download and prepare dataset

-Dataset can be found at (https://cvgl.stanford.edu/projects/uav_data/) and csv files (https://drive.google.com/drive/u/1/folders/1QpE_iRDq1hUzYNBXSBSnmfe6SgTYE3J4)

-Images and labels can be found at (https://drive.google.com/file/d/158EtAtgLMAMpQfx2nxRaWnQrug_n9rMO/view?usp=sharing)

-Video for testing the training of the model can be found at (https://drive.google.com/file/d/1FshjJtc0D3VfTIT1fPaHtFW_lMPo6vEe/view?usp=sharing)

-After downloading the dataset copy all images to one directory (/images/)

all_annotations.csv -> includes image name, x-y coordinates of top left corner of bounding box ,x-y coordinates of bottom right corner of bounding box and name of category. This csv file was created manually by copying train_annotations.csv, val_annotations.csv and test_annotations.csv to one csv file (all_annotations.csv).

```
-python3 resImgsize.py
```

resImgsize.py -> gets minimum width and height of all images dimensions and resize all images to these new dimensions.

```
-python3 csv2txt.py
```

csv2txt.py -> takes the names of images and creates corresponding txt files in (PyTorch_YOLOv4/stanford_drone_dataset/labels/) directory. Then, takes the annotations from 'all_annotations.csv', Normalize the coordinates of bounding boxes and gives an attribute to each category. Outputs are: txt files that have the name of the image they correspond and include the attributes of objects which detect the bounding box and the normalized coordinates(x,y,w,h) of each bounding box.

```
-python3 splitter.py
```

splitter.py -> splits the dataset to train set, test set and validation set. 80% of images are in train set and remaining 20% of images go to test set and validation equally.

-Modification of coco.yaml file. Rename coco.yaml to ssd.yaml and include the paths of train, val and test set , number (6) and name of classes.


## Requirements
```
pip install -r requirements.txt
```

## Training using docker

```
Build docker 
docker build -t pytorchdocker/run1 .

Run docker with GPUs

docker run -it --gpus all pytorchdocker/run1 train.py
```

## Training without docker

```
python3 train.py
```
