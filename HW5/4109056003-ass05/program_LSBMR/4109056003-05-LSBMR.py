# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 01:05:08 2023

@author: blodg
"""

import cv2
import os
import numpy as np
import random

myPath = '../'
allList = os.walk(myPath)

ratio = 0.6

def lsb(a):
    
    binary_a = bin(a)
    return int(binary_a[-1])

def lsbmr(y, y2, msg, msg2):
   
    
    if msg == lsb(y):
        if msg2 != lsb(y//2 + y2):
        
            random.seed(200)
            rnd = random.randint(0, 1)
            Y2 = y2 + 1 if rnd == 0 else y2-1
            
        else:
            Y2 = y2
        Y = y
        
    else:
        if msg2 == lsb( (y-1)//2 + y2) :
            Y = y-1
        else :
            Y = y+1
            
        Y2 = y2
        
    return Y,Y2

      

for root, dirs, files in allList:
    # print(root)
    if root == '../cover' :
        for file in files:
            # print(file)
            img = cv2.imread(root+'/'+file,cv2.IMREAD_GRAYSCALE)
            
            # secrect msg
            msg = []
            random.seed(100)
            
            for i in range(0, int(len(img[0])*len(img[1])*ratio) ):
                msg.append(random.randint(0,1))
            
            count = 0
            
            for i in range(len(img)) :
                for j in range(0,len(img[i]),2) :
                    if count >= int(len(img)*len(img[0])*ratio) :
                        break
                    
                    y, y2 = lsbmr(img[i][j],img[i][j+1],msg[i*len(img[i])+j],msg[i*len(img[i])+j+1])
                    
                    img[i][j] = y
                    img[i][j+1] = y2
                    
                    count+=2
            
            outname = file.split('.')[0]+'_stego_'+str(ratio)+'.png'
            cv2.imwrite('../stego/'+outname, img)
            