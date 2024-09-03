# -*- coding: utf-8 -*-
"""
Created on Mon May  1 19:56:51 2023

@author: blodg
"""

import cv2
import os
import numpy as np
import random

random.seed(100)

myPath = './'
allList = os.walk(myPath)

a,b = 1,1
G = 150

def RP(img):
    string = ''
    b_img = bin(img)
    b_bit =  b_img[2:]
    
    for i in range(8-len(b_bit)):
        string += '0'
    
    b_bit = list(string + b_bit)
    
    for i in range(7,0,-1):
        j = random.randint(0, i)
        b_bit[i],b_bit[j] =  b_bit[j],b_bit[i]
        
    return int(''.join(b_bit), 2)
    
    
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
            
            for i in range(0,len(img)):
                for j in range(0 , len(img)):
                    img[i][j] = RP(img[i][j])
            
            outname = file.split('.')[0]+'_enc.png'
            cv2.imwrite('./encryp/'+outname, img)