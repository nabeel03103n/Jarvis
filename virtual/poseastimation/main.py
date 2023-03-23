import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture(0)
pTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BAYER_BG2BGR)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks())
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img,results.pose_landmarks)

    cTime = time.time() 
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)

    cv2.imshow("Image",img)
    cv2.waitKey(1)