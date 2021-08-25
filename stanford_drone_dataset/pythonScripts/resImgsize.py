import cv2
import pdb
import os, sys

#path = "/home/blackandyellow/PyTorch_YOLOv4/stanford_drone_dataset/OrigImg/"
path = '/mnt/c/Users/manol/Documents/TUB_Master/4th_Semester/ProjectCV/PyTorch_YOLOv4/stanford_drone_dataset/OrigImg/'
dirs = os.listdir(path)

minWidth  = 5000
minHeight = 5000

for item in dirs:
    im = cv2.imread(path + item)
    width  = im.shape[1]
    height = im.shape[0]
    if minWidth > width: # Find minimum Width and height
        minWidth  = width
    if minHeight > height:
        minHeight = height

def resize(x, mW, mH):
    for item in dirs:
        im    = cv2.imread(path + item)
        imRes = cv2.resize(im, (minWidth, minHeight))
        #imRes = im.resize(minWidth, minHeight)
        cv2.imwrite(out_path + item, imRes)

out_path ='/mnt/c/Users/manol/Documents/TUB_Master/4th_Semester/ProjectCV/PyTorch_YOLOv4/stanford_drone_dataset/images/'
#fold = os.makedirs(str(out_path))
resize(out_path, minWidth, minHeight)



