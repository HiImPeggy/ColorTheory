# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 23:48:39 2023

@author: blodg
"""

import cv2
import os
import numpy as np


myPath = '../'
allList = os.walk(myPath)

# R_mean = {}

for root, dirs, files in allList:
    # print(root)
    if root == '../source' or root == '../target':
        for file in files:
            
            # print(file)
            img = cv2.imread(root+'/'+file)
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            R, G, B = cv2.split(img)
            
            index = index = file.index('.')
            file_name = file[:index]
            
            destination = open('../feature/'+file_name+'_dec.csv','w')
            
            destination.write( np.array2string(round(np.mean(R),2))+'\n' )
            destination.write( np.array2string(round(np.std(R),2))+'\n' )
            # R_mean[file] = round(np.mean(R),2)
            
            destination.write( np.array2string(round(np.mean(G),2))+'\n' )
            destination.write( np.array2string(round(np.std(G),2))+'\n' )
            
            destination.write( np.array2string(round(np.mean(B),2))+'\n' )
            destination.write( np.array2string(round(np.std(B),2))+'\n' )
            
            destination.close()