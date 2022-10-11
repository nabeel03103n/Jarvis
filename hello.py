# # from cgitb import text
# # from re import search
# # from tkinter import Frame
# # from cv2 import CHAIN_APPROX_NONE, RETR_EXTERNAL, VideoCapture, findContours, imshow, imwrite, waitKey
# # from gtts import gTTS
# # import os
# # from playsound import playsound
# # from pyttsx3 import speak
# # from time import sleep
# # import cv2
# # import googletrans
# # from googlesearch import search
# # import pyautogui as p
# # from pytesseract import pytesseract
# # from PIL import Image
# # from urllib.request import urlopen
# # import pyjoke
# # import pyjokes
# # import random
# # import smtplib
# # import numpy as np
# # from sklearn.metrics import pairwise




# # # load the required trained XML classifiers
# # # https://github.com/Itseez/opencv/blob/master/
# # # data/haarcascades/haarcascade_frontalface_default.xml
# # # Trained XML classifiers describes some features of some
# # # object we want to detect a cascade function is trained
# # # from a lot of positive(faces) and negative(non-faces)
# # # images.
# # # face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
  
# # # https://github.com/Itseez/opencv/blob/master
# # # /data/haarcascades/haarcascade_eye.xml
# # # Trained XML file for detecting eyes
# # # eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 
  
# # # capture frames from a camera
# # # cap = cv2.VideoCapture(0)
  
# # # # loop runs if capturing has been initialized.
# # # while 1: 
  
# # #     # reads frames from a camera
# # #     ret, img = cap.read() 
  
# # #     # convert to gray scale of each frames
# # #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
# # #     # Detects faces of different sizes in the input image
# # #     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  
# # #     for (x,y,w,h) in faces:
# # #         # To draw a rectangle in a face 
# # #         cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
# # #         roi_gray = gray[y:y+h, x:x+w]
# # #         roi_color = img[y:y+h, x:x+w]
  
# # #         # Detects eyes of different sizes in the input image
# # #         eyes = eye_cascade.detectMultiScale(roi_gray) 
  
# # #         #To draw a rectangle in eyes
# # #         for (ex,ey,ew,eh) in eyes:
# # #             cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
  
# # #     # Display an image in a window
# # #     cv2.imshow('img',img)
  
# # #     # Wait for Esc key to stop
# # #     k = cv2.waitKey(30) & 0xff
# # #     if k == 27:
# # #         break
  
# # # # Close the window
# # # cap.release()
  
# # # # De-allocate any associated memory usage
# # # cv2.destroyAllWindows() 



# # # cap = cv2.VideoCapture(0)
# # # kernelOpen = np.ones((5,5))
# # # kernelClose = np.ones((20,20))
# # # lb = np.array([20,100,100])
# # # ub = np.array([120,255,255])

# # # while True:
# # #     ret,frame = cap.read()
# # #     flipped = cv2.flip(frame, 1)
# # #     flipped = cv2.resize(flipped,(500,400))

# # #     imgSeg = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
# # #     imgSegFlipped = cv2.flip(imgSeg,1)
# # #     imgSegFlipped = cv2.resize(imgSegFlipped,(500,400))

# # #     mask = cv2.inRange(imgSegFlipped,lb,ub)
# # #     mask = cv2.resize(mask,(500,400))

# # #     maskOpen = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
# # #     maskOpen = cv2.resize(maskOpen,(500,400))
# # #     maskClose = cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
# # #     maskClose = cv2.resize(maskClose,(500,400))

# # #     final = maskClose
# # #     conts,h = cv2.findContours(maskClose,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

# # #     if(len(conts)!=0):
# # #         b = max(conts,key=cv2.contourArea)
# # #         west = tuple(b[b[:,:,0].argmin()][0])
# # #         east = tuple(b[b[:,:,0].argmax()][0])
# # #         north = tuple(b[b[:,:,1].argmin()][0])
# # #         south = tuple(b[b[:,:,1].argmax()][0])
# # #         centre_x = (west[0]+east[0])/2
# # #         centre_y = (north[0]+south[0])/2

# # #         cv2.drawContours(flipped,b,-1,(0,255,0),3)
# # #         cv2.circle(flipped,west,6,(0,0,255),-1)
# # #         cv2.circle(flipped,east,6,(0,0,255),-1)
# # #         cv2.circle(flipped,north,6,(0,0,255),-1)
# # #         cv2.circle(flipped,south,6,(0,0,255),-1)
# # #         cv2.circle(flipped,(int(centre_x),int(centre_y)),6,(255,0,0),-1)

# # #     cv2.imshow('video',flipped)
# # #     if cv2.waitKey(1) & 0xFF == ord(' '):
# # #         break

# # # cap.release()
# # # cv2.destroyAllWindows()






# # # sender = 'from@fromdomain.com'
# # # receivers = ['to@todomain.com']

# # # message = """From: From Person <from@fromdomain.com>
# # # To: To Person <to@todomain.com>
# # # Subject: SMTP e-mail test

# # # This is a test e-mail message.
# # # """

# # # try:
# # #    smtpObj = smtplib.SMTP('localhost')
# # #    smtpObj.sendmail(sender, receivers, message)         
# # #    print("Successfully sent email")

# # # except SMTPException:
# # #    print ("Error: unable to send email")


# # # with open("quiz//questions.txt")as f:
# # #     words = ("word","nabeel","Aman")
# # #     f1 = random.choices(f)
# # #     print(f1)

# # # My_joke = pyjokes.get_joke(language="en", category="all")
# # # print(My_joke)
# # # speak(My_joke)


# # # url = "https://www.instagram.com/direct/t/340282366841710300949128275173812566689"
# # # page = urlopen(url)
# # # html_bytes = page.read()
# # # html = html_bytes.decode("utf-8")
# # # print(html)

# # # print(p.position())




# # # query = input("Enter:\n")
# # # for j in search(query,tld='co.in',num=1,stop=1,pause=2):
# # #     print(j)

# # # print('File name :    ', os.path.basename(__file__))
# # # print('Directory Name:     ', os.path.dirname(__file__))


# # # translator = googletrans.Translator()

# # # text00 = "how can i help you"

# # # text0 = translator.translate(text00,src='en',dest='hi')
# # # text1 = text0.text
# # # speak = gTTS(text=text1,lang='hi',slow=False)
# # # speak.save("test.mp3")
# # # os.system("test.mp3")


# # # t = gTTS('मुझे बताएं कि मैं आपकी कैसे मदद कर सकता हूं')
# # # t.save("t.mp3")
# # # playsound('t.mp3')

# # # cam_port = 0
# # # cam = VideoCapture(0)

# # # result, image = cam.read()

# # # if result:
# # #     imshow("Nabeel ali khan",image)
# # #     imwrite("nabeel.png",image)
# # #     waitKey(0)
# # # else:
# # #     print("no")

# # import googlenews
# # print(googlenews.get_news('APPLE'))

# # OpenCV program to detect face in real time
# # import libraries of python OpenCV
# # where its functionality resides
# import cv2

# # load the required trained XML classifiers
# # https://github.com/Itseez/opencv/blob/master/
# # data/haarcascades/haarcascade_frontalface_default.xml
# # Trained XML classifiers describes some features of some
# # object we want to detect a cascade function is trained
# # from a lot of positive(faces) and negative(non-faces)
# # images.
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# # https://github.com/Itseez/opencv/blob/master
# # /data/haarcascades/haarcascade_eye.xml
# # Trained XML file for detecting eyes
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# # capture frames from a camera
# cap = cv2.VideoCapture(0)

# # loop runs if capturing has been initialized.
# while 1:

# 	# reads frames from a camera
# 	ret, img = cap.read()

# 	# convert to gray scale of each frames
# 	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 	# Detects faces of different sizes in the input image
# 	faces = face_cascade.detectMultiScale(gray, 1,3, 5)

# 	for (x,y,w,h) in faces:
# 		# To draw a rectangle in a face
# 		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
# 		roi_gray = gray[y:y+h, x:x+w]
# 		roi_color = img[y:y+h, x:x+w]

# 		# Detects eyes of different sizes in the input image
# 		eyes = eye_cascade.detectMultiScale(roi_gray)

# 		#To draw a rectangle in eyes
# 		for (ex,ey,ew,eh) in eyes:
# 			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)

# 	# Display an image in a window
# 	cv2.imshow('img',img)

# 	# Wait for Esc key to stop
# 	k = cv2.waitKey(30) & 0xff
# 	if k == 27:
# 		break

# # Close the window
# cap.release()

# # De-allocate any associated memory usage
# cv2.destroyAllWindows()


# import tensorflow

import pyautogui as p

print(p.position())
