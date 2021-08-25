import cv2
import pdb
import os, sys

path = "/home/manolis/Desktop/ComputerVision/ProjectCV/PyTorch_YOLOv4/stanford_drone_dataset/images/"
dirs = os.listdir(path)

#dirs = dirs[:1000]

#sizes = list()

minWidth  = 5000
minHeight = 5000

for item in dirs:
    im = cv2.imread(path + item)
    imgSizHeight  = im.shape[0]
    imgSizWidth   = im.shape[1]
    
    print('width = {} , height = {}'.format(imgSizWidth , imgSizHeight))
 
    if minWidth > imgSizWidth: # Find minimum Width and height
        minWidth  = imgSizWidth
    if minHeight > imgSizHeight:
        minHeight = imgSizHeight

print('Minimum width = {} , Minimum height = {}'.format(minWidth , minHeight))
