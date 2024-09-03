# -*- coding: utf-8 -*-
"""
Created on Mon May  1 20:29:09 2023

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

def RRP(img):
    string = ''
    r = []
    
    b_img = bin(img)
    b_img = b_img[2:]

    for i in range(8-len(b_img)):
        string += '0'
        
    b_img = list(string + b_img)
    
    for i in range(7,0,-1):
        r.append(random.randint(0, i))
    
    r.reverse()
    
    for i in range(1,8):
        b_img[i],b_img[r[i-1]] = b_img[r[i-1]] , b_img[i]
        
    return int(''.join(b_img), 2)


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
            # print(img.shape)
            
            for i in range(0,len(img)):
                for j in range(0 , len(img)):
                    img[i][j] = RRP(img[i][j])
                    
            img = cal(img.shape[0],img)
            
            outname = file.split('_')[0]+'_dec.png'
            cv2.imwrite('./decryp/'+outname, img)