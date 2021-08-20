# -*- coding: utf-8 -*-
"""CountWheatgrains.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hq7okEQOhk-GUW0MlvWZFMkNuk8Tbzz8
"""



import cv2
import matplotlib.pyplot as plt



def count():
    image = cv2.imread('/home/knoldus/Downloads/rice-quality-analysis-master (1)/Rice-Grain-Image-Classification-master/static/inputImage.jpg')

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    plt.imshow(gray, cmap='gray')

    blur = cv2.GaussianBlur(gray, (11, 11), 0)
    plt.imshow(blur, cmap='gray')

    canny = cv2.Canny(blur, 30, 150, 3)
    plt.imshow(canny, cmap='gray')

    dilated = cv2.dilate(canny, (1, 1), iterations=1)
    plt.imshow(dilated, cmap='gray')

    (cnt, heirarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)
    plt.imshow(rgb)
    print('grains in the image', len(cnt))
    return  len(cnt)








