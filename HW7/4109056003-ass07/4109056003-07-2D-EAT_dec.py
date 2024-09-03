# -*- coding: utf-8 -*-
"""
Created on Mon May  1 20:29:09 2023

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
    xmap = (x - a*y) % N
    ymap = (-b*x + (a*b+1)*y) % N
    
    for r in range(G):
        img = img[xmap, ymap]
        
    return img
    

for root, dirs, files in allList:
    # print(root)
    if 'encryp' in root :
        for file in files:
            # print(file)
            img = cv2.imread(root+'/'+file,cv2.IMREAD_GRAYSCALE)
            img = cal(img.shape[0],img)
            
            outname = file.split('_')[0]+'_dec.png'
            cv2.imwrite('./decryp/'+outname, img)