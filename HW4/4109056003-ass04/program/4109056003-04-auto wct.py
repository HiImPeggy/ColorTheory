# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 21:40:48 2023

@author: blodg
"""

import cv2
import os
import numpy as np
import csv

myPath = '../'
allList = os.walk(myPath)

final_weight = [-1,-1,-1]
final_dis = [-1,-1,-1]

def image_stats(image):

    (l, a, b) = cv2.split(image)
    (lMean, lStd) = ( round(l.mean(),2) , round(l.std(),2) )
    (aMean, aStd) = ( round(a.mean(),2) , round(a.std(),2) )
    (bMean, bStd) = ( round(b.mean(),2) , round(b.std(),2) )

    return (lMean, lStd, aMean, aStd, bMean, bStd)

def color_transfer(source, target, weight, channe):

    source = source.astype("float32")
    target = target.astype("float32")
    
    
    (lMeanSrc, lStdSrc, aMeanSrc, aStdSrc, bMeanSrc, bStdSrc) = image_stats(source)
    (lMeanTar, lStdTar, aMeanTar, aStdTar, bMeanTar, bStdTar) = image_stats(target)

    (l, a, b) = cv2.split(source)
    l -= lMeanSrc
    a -= aMeanSrc
    b -= bMeanSrc

    l = (weight*lStdTar + (1 - weight)*lStdSrc)*l / lStdSrc
    a = (weight*aStdTar + (1 - weight)*aStdSrc)*a / aStdSrc
    b = (weight*bStdTar + (1 - weight)*bStdSrc)*b / bStdSrc
    l += (lMeanTar*weight)
    a += (aMeanTar*weight)
    b += (bMeanTar*weight)
    
    l += (lMeanSrc*(1-weight))
    a += (aMeanSrc*(1-weight))
    b += (bMeanSrc*(1-weight))

    l = np.clip(l, 0, 255)
    a = np.clip(a, 0, 255)
    b = np.clip(b, 0, 255)

    transfer = cv2.merge([l, a, b])
    transfer = transfer.astype("uint8")
    
    return transfer

def calculate(hist1, hist2):
    
    methods = [cv2.HISTCMP_CORREL]
    
    for method in methods:
        src1_src2 = cv2.compareHist(hist1, hist2, method)
        
        if method == cv2.HISTCMP_CORREL:
            str_method = "Correlation"
        if method == cv2.HISTCMP_CHISQR:
            str_method = "Chi-square"
        if method == cv2.HISTCMP_INTERSECT:
            str_method = "Intersection"
        if method == cv2.HISTCMP_BHATTACHARYYA:
            str_method = "Bhattacharyya"
        
        # print("%s src1_src2 = %.2f"%(str_method, src1_src2))
        return src1_src2

def distance(transfer, source, target, weight, channel):
    """calculation"""
    
    hist_trf = cv2.calcHist([transfer], [channel], None, [256], [0, 256]) 
    hist_sou = cv2.calcHist([source], [channel], None, [256], [0, 256])
    hist_tar = cv2.calcHist([target], [channel], None, [256], [0, 256])
    
    sou_trf = calculate(hist_sou, hist_trf)
    tar_trf = calculate(hist_tar, hist_trf)  
    
    """"""
    dis = abs(sou_trf - tar_trf)
    
    if final_dis[channel] == -1 or final_dis[channel] > dis:
        final_dis[channel] = dis
        final_weight[channel] = weight
    # print(final_weight)
    return sou_trf, tar_trf, dis

def result(source,target):
    source = source.astype("float32")
    target = target.astype("float32")
    
    
    (lMeanSrc, lStdSrc, aMeanSrc, aStdSrc, bMeanSrc, bStdSrc) = image_stats(source)
    (lMeanTar, lStdTar, aMeanTar, aStdTar, bMeanTar, bStdTar) = image_stats(target)

    (l, a, b) = cv2.split(source)
    l -= lMeanSrc
    a -= aMeanSrc
    b -= bMeanSrc

    l = (final_weight[0]*lStdTar + (1 - final_weight[0])*lStdSrc)*l / lStdSrc
    a = (final_weight[1]*aStdTar + (1 - final_weight[1])*aStdSrc)*a / aStdSrc
    b = (final_weight[2]*bStdTar + (1 - final_weight[2])*bStdSrc)*b / bStdSrc
    l += (lMeanTar*final_weight[0])
    a += (aMeanTar*final_weight[1])
    b += (bMeanTar*final_weight[2])
    
    l += (lMeanSrc*(1-final_weight[0]))
    a += (aMeanSrc*(1-final_weight[1]))
    b += (bMeanSrc*(1-final_weight[2]))

    l = np.clip(l, 0, 255)
    a = np.clip(a, 0, 255)
    b = np.clip(b, 0, 255)

    transfer = cv2.merge([l, a, b])
    final_picture = transfer.astype("uint8")
    
    return final_picture

def readfile():
    
    for root, dirs, files in allList:
        # print(root)
        if root == '../awctresult-COR':
            for file in files:
                # print(file)
                img = cv2.imread(root+'/'+file)
                
                if file[0:3] == "sou":  
                    source.append(img)
                elif file[0:3] == "tar":   
                    target.append(img)


if __name__ == "__main__":
    
    source = []    
    target = []
    readfile()
    
    brg = {0 : "blue", 1 : "green", 2 : "red"}
    
    for i in range(0,6):
        final_weight = [-1,-1,-1]
        final_dis = [-1,-1,-1]
        
        for channel, color in brg.items():
            s = "res-0"+str(i+1)+"-dist-"+ color +".csv"
            
            with open('../distance-COR/'+s,'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Correlation Distance"])
                writer.writerow(["No","Weight","D(S, Iw)","D(T, Iw)", "Difference"])
                
                for w in np.arange(0,1.01,0.01):
                    weight = round(w,2)
                    
                    ct = color_transfer(source[i], target[i], weight, channel )
                    sou_trf, tar_trf, difference = distance(ct, source[i], target[i], weight, channel)
                    writer.writerow([i+1, weight, round(sou_trf,6), round(tar_trf,6),round(difference,6)])
         
        name = '-'+np.array2string(round(final_weight[0],2))+\
        "-"+np.array2string(round(final_weight[1],2))+\
        "-"+np.array2string(round(final_weight[2],2))
        
        out = result(source[i], target[i])
        cv2.imwrite('../awctresult-COR/res-0%d'%(i+1)+name+'.png', out)