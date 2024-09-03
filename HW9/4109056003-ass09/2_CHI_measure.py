# -*- coding: utf-8 -*-
"""
Created on Thu May 25 09:29:06 2023

@author: blodg
"""

import cv2 
import os
import numpy as np
import csv


def calCHI(img):
    
    SD = 0
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    
    exp = np.sum(hist) / 256
    for i in range(256):
        SD += np.power(hist[i][0] - exp,2)

    SD/= exp

    return SD



with open('./statis/CHI_res.csv', 'w', newline='') as f:
# 建立 CSV 檔寫入器
    writer = csv.writer(f)
    writer.writerow(['CHI', '', 'Cipher','','','','','Resullts'])
    writer.writerow(['Image', 'Type', 'Red','Green','Blue','alpha','chi value','Red','Green','Blue'])
    
    for file in os.listdir('./source/'):

        filename = file.split('.')[0] + '_enc.png'
        img = cv2.imread('./encryp/'+filename, cv2.IMREAD_GRAYSCALE)
        
        n = calCHI(img)
        
        if n < 293.248:
           writer.writerow([file, 'gray', str(n),'','','0.05','293.248','pass'])
        else:
           writer.writerow([file, 'gray', str(n),'','','0.05','293.248','fail'])
           
        
        
            


