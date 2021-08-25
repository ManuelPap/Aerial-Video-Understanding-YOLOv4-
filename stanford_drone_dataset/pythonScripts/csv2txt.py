import csv
import os
from pathlib import Path
import pdb
import cv2

path2images = '/home/blackandyellow/PyTorch_YOLOv4/stanford_drone_dataset/OrigImg'
allFiles = os.listdir('/home/blackandyellow/PyTorch_YOLOv4/stanford_drone_dataset/images/')
path = '/home/blackandyellow/PyTorch_YOLOv4/stanford_drone_dataset/labels/'

for dataFiles in allFiles:
    dataFiles = dataFiles.split('.')[0]
    f = open(path + dataFiles + ".txt", "x")
    f.close

annotFile = '/home/blackandyellow/PyTorch_YOLOv4/stanford_drone_dataset/all_annotations.csv'
pathImg = []
i = 0
with open(annotFile, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    for row in csv_reader:
        pathImg = row[0]
        pathName  = pathImg.split('/')[2]
        im = cv2.imread(os.path.join(path2images, pathName)) #read dimensions of original images
        width  = im.shape[1]
        height = im.shape[0]
        
        # Default annotations
        x1 = int(row[1])
        y1 = int(row[2])
        x2 = int(row[3])
        y2 = int(row[4])

        # Default size
        x = x1
        y = y1
        w = x2-x1
        h = y2-y1

        #Normalize the coordinates
        coord1 = (x*1322/width)/1322 #1322 is the minimum width of all images. width refers to each image.
        coord2 = (y*844/height)/848 #844 minimum height
        coord3 = (w*1322/width)/1322
        coord4 = (h*844/height)/848
        attr   = row[5]

        if attr == 'Pedestrian':
           attr = 0
        if attr == 'Biker':
           attr = 1
        if attr == 'Car':
           attr = 2
        if attr == 'Skater':
           attr = 3
        if attr == 'Cart':
           attr = 4
        if attr == 'Bus':
           attr = 5

        name  = pathImg.split('/')[2]
        name1 = name.split('.')[0] # name1 is the image name extracted from .csv
        
        f = open(path + name1 + ".txt", "a")
        f.write("{} {} {} {} {}".format(attr,coord1,coord2,coord3,coord4)+'\n')
        f.close()
