#coding: utf-8

import cv2
import numpy as np
import math

img_name = 'img_dst'
cv2.namedWindow('src')
cv2.namedWindow('dst')
cv2.namedWindow('tmp')

cap = cv2.VideoCapture(0)
while True:
    ret, img_src = cap.read() #カメラ映像の読み込み
    #ここに核となる諸理を記述
    #img_dst = cv2.flip(img_src , flipCode = 0) #垂直反転
    img_dst = cv2.medianBlur(img_src, 9)
    #img_dst = cv2.cvtColor(img_dst, cv2.COLOR_BGR2GRAY)
    img_tmp = cv2.Sobel(img_src, cv2.CV_32F, 1, 0)
    img_tmp = cv2.convertScaleAbs(img_tmp)
    img_dst = cv2.absdiff(img_src, img_tmp)
    #img_dst = cv2.cvtColor(img_tmp, cv2.COLOR_BGR2GRAY)
    cv2.imshow('src', img_src) #入力画像を表示
    cv2.imshow('dst', img_dst) #出力画像を表示
    cv2.imshow('tmp', img_tmp) #出力画像を表示
    ch = cv2.waitKey(1) #キー入力待ち

    if ch == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
