#coding: utf-8

import cv2
import numpy as np
import math

img_name = 'img_dst'
cv2.namedWindow('src')
cv2.namedWindow('dst')

cap = cv2.VideoCapture(0)
cap_before_3 = None
cap_before_2 = None
cap_before_1 = None
while True:
    ret, img_src = cap.read() #カメラ映像の読み込み
    cap_before_3 = cap_before_2
    cap_before_2 = cap_before_1
    cap_before_1 = img_src
    if cap_before_3 is not None:
        #差分画像を表示
        img_diff_1 = cv2.absdiff(cap_before_3, cap_before_2)
        img_diff_2 = cv2.absdiff(cap_before_2, cap_before_1)
        #画像の２値化
        img_diff_1_b = cv2.threshold(img_diff_1, 20, 255, cv2.THRESH_BINARY)[1]
        img_diff_2_b = cv2.threshold(img_diff_2, 20, 255, cv2.THRESH_BINARY)[1]
        #２値化した画像の共通部分
        img_m = cv2.bitwise_and(img_diff_1_b, img_diff_2_b)
        #マスク画像の生成
        op = np.ones((3,3), np.uint8)
        img_md = cv2.dilate(img_m, op, iterations =  3)
        img_msk = cv2.erode(img_md, op, iterations =  3)
        #マスクを賭ける
        img_dst = cv2.bitwise_and(cap_before_2, img_msk)
        #ここに核となる諸理を記述
        cv2.imshow('src', img_src) #入力画像を表示
        cv2.imshow('dst', img_dst) #出力画像を表示
        #cv2.imshow('tmp', img_tmp) #出力画像を表示
        ch = cv2.waitKey(1) #キー入力待ち

        if ch == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
