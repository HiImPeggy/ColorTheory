# -*- coding: utf-8 -*-
"""
Created on Thu May 25 02:34:41 2023

@author: blodg
"""

import cv2
import os
import numpy as np
import csv



def calVOH(img):
    SD = 0
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    
    for i in range(256):
        for j in range(256):
            SD += np.power(hist[i][0] - hist[j][0],2)

    SD /= (2*256*256)
    
    return SD
    
with open('./statis/VOH_res.csv', 'w', newline='') as f:
  # 建立 CSV 檔寫入器
        writer = csv.writer(f)
        writer.writerow(['VOH', '', 'Plain','','','Cipher','',''])
        writer.writerow(['Image', 'Type', 'Red','Green','Blue','Red','Green','Blue'])
        
        for file in os.listdir('./source/'):
            
            
            img = cv2.imread('./source/'+file, cv2.IMREAD_GRAYSCALE)
            n = str( calVOH(img))
            
            filename = file.split('.')[0] + '_enc.png'
            img_e = cv2.imread('./encryp/'+filename, cv2.IMREAD_GRAYSCALE)
            
            n2 = str (calVOH(img_e))
            
            writer.writerow([file, 'gray', n,'','',n2,'',''])
    