import cv2
from cvzone .HandTrackingModule import HandDetector
import numpy as np
import math
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(mode=False, maxHands=2, detectionCon=0.5, minTrackCon=0.5)

offset = 20
imgsize = 300

folder = "Data/A"  # A라는 폴더에 저장할꺼임,(폴더 바꿔주면서 데이터 저장)
counter = 0

while True:
    success, img = cap.read()
    Hands, img = detector.findHands(img)
    if Hands:
        # 이미지 분할
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imgWhite = np.ones((imgSize, imgsize, 3), np.uint8)*255

        imgCrop = img[y-offset:y+h+offset, x-offset:x+w+offset]

        imgCropshape = imgCrop.shape
        imgWhite[0:imgCropshape[0], 0:imgCropshape[1]] = imgCrop

        aspectRatio = h/w

        if aspectRatio >1 :
            k = imgsize/h
            wCal = math.cell(w+k)
            imgResize = cv2.resize(imgCrop, (wCal, imgsize))
            imgReshape = imgResize.shape
            wGap = math.cell((300-wCal)/2)
            imgWhite[:, wGap:wCal+wGap] = imgResize
        else:
            k = imgsize / w
            hCal = math.cell(h + k)
            imgResize = cv2.resize(imgCrop, (imgsize, hCal))
            imgReshape = imgResize.shape
            hGap = math.cell((300 - hCal) / 2)
            imgWhite[wGap:wCal + wGap, :] = imgResize


        cv2.imshow('Hand', imgCrop)
        cv2.imshow('Hand', imgWhite)


    cv2.imshow('Hand', img)
    key = cv2.waitkey(1)
    if key == ord("s"): # s 누르면 데이터 저장
        counter += 1
        cv2.imwrite(f'{folder}/image_{time.time()}.jpg', imgWhite)
        print(counter)