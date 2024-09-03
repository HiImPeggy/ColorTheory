# -*- coding: utf-8 -*-
"""
Created on Thu May 25 09:41:41 2023

@author: blodg
"""

import cv2 
import os
import numpy as np
import csv


def calCIE(image):
    

    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    sum_up = np.sum(hist)  
    probibility = [i/sum_up for i in hist]
   
    e = 1e-8
    probibility = np.maximum(probibility, e)
    
    entropy = -np.sum(probibility * np.log2(probibility))
    return entropy




with open('./statis/GIE_res.csv', 'w', newline='') as f:
# 建立 CSV 檔寫入器
    writer = csv.writer(f)
    writer.writerow(['GIE', '', 'Plain','','','Cipher'])
    writer.writerow(['Image', 'Type', 'Red','Green','Blue','Red','Green','Blue'])
    
    for file in os.listdir('./source/'):
    
    
        img = cv2.imread('./source/'+file, cv2.IMREAD_GRAYSCALE)
        n = calCIE(img)
        
        filename = file.split('.')[0] + '_enc.png'
        img_e = cv2.imread('./encryp/'+filename, cv2.IMREAD_GRAYSCALE)
        n2 = calCIE(img_e)

        writer.writerow([file, 'gray', str(n),'','',str(n2)])
      



