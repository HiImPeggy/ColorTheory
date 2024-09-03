# -*- coding: utf-8 -*-
"""
Created on Mon May  1 19:56:51 2023

@author: blodg
"""

import cv2
import os
import numpy as np

myPath = './'
allList = os.walk(myPath)

a,b = 1,1
G = 150

def cal(N,img):
    x, y = np.meshgrid(range(N), range(N), indexing="ij")
    xmap = (a*b*x + x +a*y) % N
    ymap = (b*x + y) % N
    
    for r in range(G):
        img = img[xmap, ymap]
        
        
    return img
    

for root, dirs, files in allList:
    # print(root)
    if 'source' in root :
        for file in files:
            # print(file)
            image = cv2.imread(root+'/'+file,cv2.IMREAD_GRAYSCALE)
            img = cal(image.shape[0],image)
            
            outname = file.split('.')[0]+'_enc.png'
            cv2.imwrite('./encryp/'+outname, img)