import cv2
import cvzone

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

# 689 393
#1024 115

while True:
    imgBg = cv2.imread("Resources/bg.png")
    success, img  = cap.read()
    imgScalled = cv2.resize(img,(0,0),None,0.600,0.800)
    imgScalled = imgScalled[80:600,50:680]

    imgBg[115:393,1024:689] = imgScalled

    cv2.waitKey(1)
    cv2.imshow("Image1",imgBg)
    cv2.imshow("Image",img)
    cv2.imshow("Scale",imgScalled)
    