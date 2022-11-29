import cv2
from cvzone.HandTrackingModule import HandDetector
import pydirectinput as pd


cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)
 
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # With Draw
    # hands = detector.findHands(img, draw=False)  # No Draw
 
    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmarks points
        bbox1 = hand1["bbox"]  # Bounding Box info x,y,w,h
        centerPoint1 = hand1["center"]  # center of the hand cx,cy
        handType1 = hand1["type"]  # Hand Type Left or Right
 
        # print(len(lmList1),lmList1)
        # print(bbox1)
        # print(centerPoint1)
        fingers1 = detector.fingersUp(hand1)
        #length, info, img = detector.findDistance(lmList1[8], lmList1[12], img) # with draw
        #length, info = detector.findDistance(lmList1[8], lmList1[12])  # no draw
 
 
        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmarks points
            bbox2 = hand2["bbox"]  # Bounding Box info x,y,w,h
            centerPoint2 = hand2["center"]  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type Left or Right
 
            fingers2 = detector.fingersUp(hand2)
            # print(fingers1, fingers2)
            #length, info, img = detector.findDistance(lmList1[8], lmList2[8], img) # with draw
            length, info, img = detector.findDistance(centerPoint1, centerPoint2, img)  # with draw

            if  sum(fingers2)==5 and sum(fingers1)==0:
                    pd.keyUp('d')
                    pd.keyUp('s')
                    pd.keyUp('x')
                    pd.keyUp('space')
                    pd.keyDown('a')

            elif sum(fingers1)==5 and sum(fingers2)==0:
                    pd.keyUp('a')
                    pd.keyUp('s')
                    pd.keyUp('space')
                    pd.keyUp('x')
                    pd.keyDown('d')


            elif fingers1[1]==1:
                    pd.keyUp('a')
                    pd.keyUp('d')
                    pd.keyUp('s')
                    pd.keyUp('x')
                    pd.keyUp('space')
                    pd.keyDown('w')


            elif fingers2[1]==1:
                    pd.keyUp('a')
                    pd.keyUp('d')
                    pd.keyUp('s')
                    pd.keyUp('w')
                    pd.keyUp('x')
                    pd.keyDown('space')     

            elif fingers2[2]==1:
                    pd.keyUp('a')
                    pd.keyUp('d')
                    pd.keyUp('s')
                    pd.keyUp('space')
                    pd.keyDown('x')

            elif sum(fingers1)==0 and sum(fingers2)==0:
                    pd.keyUp('a')
                    pd.keyUp('d')
                    pd.keyUp('w')
                    pd.keyUp('space')
                    pd.keyUp('x')
                    pd.keyDown('s')                


    # cv2.imshow("Image", img)
    cv2.waitKey(1)