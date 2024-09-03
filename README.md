# ColorTheory

## Assignment 01: 擷取影像統計特徵值

**內容**：

計算出source 和 target 中的平均值和標準差，並以RGB的順序填入excel檔中。

## Assignment 02-Basic Color Transfer

**內容**：

將target和source使用basic color transfer進行色彩轉換。

**結果**：

![image](https://github.com/user-attachments/assets/fde7b0c3-07f0-4d76-822a-5f5b8ad8885e)

## Assignment 03: Ordinary Color Transfer

**內容**：

將target和source使用Ordinary Color Transfer進行色彩轉換，和作業2差別於使用的色彩空間會經lαβ轉換。

**結果**：
 
![image](https://github.com/user-attachments/assets/2a748ef7-bf9a-48b1-af31-60be5c814ba6)


## Assignment 04:Automatic Weighted Color Transfer

**內容**：

使用Weighted Color Transfer (WCT)，並根據第 2 個作業Basic Color Transfer 的程式修正，使用0-1，共100個不同權重，運用暴力解，找出最恰當的權重。

**結果**：

![image](https://github.com/user-attachments/assets/0f3430d0-0a9f-4495-aaf0-f39b49c0c249)


## Assignment 05: LSB Matching Revisited

**內容**：

運用LSBMR演算法，根據LSB的值，決定欲遷入之秘密訊息，Ratio會決定嵌入訊息的像素為何。

**結果**：

![image](https://github.com/user-attachments/assets/26024d6b-57be-45e5-8a73-11ef73a53fc5)

## Assignment 06: LSB-K and OPAP-K Comparison

**內容**：

證明MSE(LSB-k)和MSE(OPAP-k)的公式，並依據兩個公式，寫出各別的(1) embedding rate; (2) mean square error; (3) PSNR; (4) embedding efficiency



## Assignment 07: 2D EAT for image encryption

**內容**：

使用2D Equilateral Arnold Transform對影像加密，將會以不同的(a,b)值建構矩陣，並以此矩陣做訊息加密，G將會決定訊息加密的次數。

**結果**：

![image](https://github.com/user-attachments/assets/4a521875-abbf-410e-8e57-efbd04626315)

![image](https://github.com/user-attachments/assets/cfe8bb73-c135-4cc5-8118-73809fb4af7c)


## Assignment 08: Image Encryption by 2D EAT and Random Permutation

**內容**：

使用2D Equilateral Arnold Transform對影像加密，並以Durstenfeld 的 RP 演算法依據 7 個隨機整數做排列，最後也會以此7個隨機整數搭配EAT作解密。

**結果**：

![image](https://github.com/user-attachments/assets/0a65c919-4d46-491c-b83d-eda7bdd595b7)

![image](https://github.com/user-attachments/assets/e775198d-abe3-488a-a06b-b77c74338e63)

## Assignment 09: Metrics for image encryption

**內容**：

算出以EAT加密後的影像和加密前的影像之間 (1) variance of histogram (VOH); (2) Chi-square test; (3) Pear correlation coefficients; (4) Global information entropy。

