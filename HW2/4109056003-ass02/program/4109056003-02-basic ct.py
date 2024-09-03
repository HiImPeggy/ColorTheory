# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 00:42:07 2023

@author: blodg
"""

import cv2
import os
import numpy as np


myPath = '../'
allList = os.walk(myPath)

def image_stats(image):

    (l, a, b) = cv2.split(image)
    (lMean, lStd) = ( round(l.mean(),2) , round(l.std(),2) )
    (aMean, aStd) = ( round(a.mean(),2) , round(a.std(),2) )
    (bMean, bStd) = ( round(b.mean(),2) , round(b.std(),2) )

    return (lMean, lStd, aMean, aStd, bMean, bStd)

def color_transfer(source, target):

    source = cv2.cvtColor(source, cv2.COLOR_BGR2LAB).astype("float32")
    target = cv2.cvtColor(target, cv2.COLOR_BGR2LAB).astype("float32")

    (lMeanSrc, lStdSrc, aMeanSrc, aStdSrc, bMeanSrc, bStdSrc) = image_stats(source)
    (lMeanTar, lStdTar, aMeanTar, aStdTar, bMeanTar, bStdTar) = image_stats(target)

    (l, a, b) = cv2.split(target)
    l -= lMeanTar
    a -= aMeanTar
    b -= bMeanTar

    l = (lStdTar / lStdSrc) * l
    a = (aStdTar / aStdSrc) * a
    b = (bStdTar / bStdSrc) * b

    l += lMeanSrc
    a += aMeanSrc
    b += bMeanSrc

    l = np.clip(l, 0, 255)
    a = np.clip(a, 0, 255)
    b = np.clip(b, 0, 255)

    transfer = cv2.merge([l, a, b])
    transfer = cv2.cvtColor(transfer.astype("uint8"), cv2.COLOR_LAB2BGR)
    
    return transfer 


source = []    
target = []

for root, dirs, files in allList:
    # print(root)
    if root == '../bctresult':
        for file in files:
            # print(file)
            img = cv2.imread(root+'/'+file)
            
            if file[0:3] == "sou":  
                source.append(img)
            elif file[0:3] == "tar":   
                target.append(img)

for i in range(0,6):
    out = color_transfer(source[i], target[i])
    # cv2.imshow('My Image', out)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    cv2.imwrite('../bctresult/res-0%d.png'%(i+1), out)
        
