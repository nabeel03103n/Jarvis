import cv2
import numpy as np
import HandTrackingModule as htm
import time
import pyautogui as p
from pyttsx3 import speak


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

detector = htm.handDetector(maxHands=2)
wScr, hScr = p.size()


while True:
    # Step1: Find the landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # Step2: Get the tip of the index and middle finger
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        # Step3: Check which fingers are up
        fingers = detector.fingersUp()

        allFingers = fingers[0]==1 and fingers[1]==1 and fingers[2]==1 and fingers[3]==1 and fingers[4]==1
        fingers4 = fingers[0]==0 and fingers[1]==1 and fingers[2]==1 and fingers[3]==1 and fingers[4]==1
        fingers3 = fingers[0]==0 and fingers[1]==1 and fingers[2]==1 and fingers[3]==1 and fingers[4]==0

        if allFingers:
            cv2.putText(img, str("Hello"), (50, 250), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

        elif fingers[0]==0 and fingers[1]==0 and fingers[2]==1 and fingers[3]==0 and fingers[4]==0:
            cv2.putText(img, str("Fuck you"), (50, 250), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 8), 3)

        elif fingers[0]==0 and fingers[1]==0 and fingers[2]==0 and fingers[3]==0 and fingers[4]==1:
            cv2.putText(img, str("I need to pee"), (50, 250), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 3)

        elif fingers[0]==0 and fingers[1]==1 and fingers[2]==0 and fingers[3]==0 and fingers[4]==0:
            cv2.putText(img, str("ALLAH HU AKBAR"), (50, 250), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        elif fingers[0]==0 and fingers[1]==0 and fingers[2]==0 and fingers[3]==1 and fingers[4]==0:
            cv2.putText(img, str("I'm Nabeel"), (50, 250), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 8), 3)


        



    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (28, 58), cv2.FONT_HERSHEY_PLAIN, 3, (255, 8, 8), 3)

    # Step12: Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)