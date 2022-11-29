import cv2
import numpy as np
import HandTrackingModule as htm
import time
import pyautogui as p
import os
import pydirectinput as pd
from pyttsx3 import speak


######################
wCam, hCam = 640, 480
frameR = 100     #Frame Reduction
smoothening = 7  #random value
######################

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(maxHands=1)
wScr, hScr = p.size()

# print(wScr, hScr)

while True:
    # Step1: Find the landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # Step2: Get the tip of the index and middle finger
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        px1,py1 = lmList[8][1],lmList[8][2]
        px2,py2 = lmList[6][1],lmList[6][2]
        # print(px1,py1)

        # Step3: Check which fingers are up
        fingers = detector.fingersUp()
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                      (255, 0, 255), 2)


        if fingers[1]==1 and fingers[2] == 0 and fingers[0]==0 and fingers[3]==0 and fingers[4]==0:
            pd.keyUp('right')
            pd.keyUp('left')
            speak("Nothing")

        # if fingers[4]==1 and fingers[0]==0 and fingers[1]==0 and fingers[2]==0 and fingers[3]==0:
        #     pd.keyUp('a')
        #     pd.keyUp('s')
        #     pd.keyUp('space')
        #     pd.keyUp('x')
        #     pd.keyDown('d')

        # if fingers[4]==0 and fingers[0]==1 and fingers[1]==0 and fingers[2]==0 and fingers[3]==0:
        #     pd.keyUp('a')
        #     pd.keyUp('d')
        #     pd.keyUp('s')
        #     pd.keyUp('space')
        #     pd.keyDown('x')

        # if fingers[4]==0 and fingers[0]==0 and fingers[1]==1 and fingers[2]==1 and fingers[3]==0:
        #     pd.keyUp('a')
        #     pd.keyUp('d')
        #     pd.keyUp('w')
        #     pd.keyUp('space')
        #     pd.keyUp('x')
        #     pd.keyDown('s')

        if fingers[4]==1 and fingers[1]==1 and fingers[1]==1 and fingers[2]==1 and fingers[3]==1:
            pd.keyUp('left')
            pd.keyDown('right')
            speak('gas')

        if fingers[1]==0 and fingers[2] == 0 and fingers[0]==0 and fingers[3]==0 and fingers[4]==0:
            pd.keyUp('right')
            pd.keyDown('left')
            speak('brake')



    # Step11: Frame rate
    # cTime = time.time()
    # fps = 1/(cTime-pTime)
    # pTime = cTime
    # cv2.putText(img, str(int(fps)), (28, 58), cv2.FONT_HERSHEY_PLAIN, 3, (255, 8, 8), 3)

    # Step12: Display
    # cv2.imshow("Image", img)
    cv2.waitKey(1)