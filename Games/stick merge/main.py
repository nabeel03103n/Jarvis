import pyautogui as p
from time import sleep
from pyttsx3 import speak

#Global Vars
main = 'main.png'
target = 'target.png'
target1 = 'target1.png'
target2 = 'target2.png'
target3 = 'target3.png'

def locating():

    while True:
        locate_main = p.locateOnScreen(main,confidence=0.9,grayscale=True)
        locate_stickman = p.locateOnScreen(target,confidence=0.8,grayscale=True)
        locate_stickman1 = p.locateOnScreen(target1,confidence=0.8,grayscale=True)
        locate_stickman2 = p.locateOnScreen(target2,confidence=0.8,grayscale=True)
        locate_stickman3 = p.locateOnScreen(target3,confidence=0.8,grayscale=True)

        if locate_main != None:
            speak('I can see the main target')
            print('I can see the main target')
            p.click(locate_main)

        if locate_stickman != None:
            print('I can see the target number 1')
            speak('I can see the target number 1')
            p.click(locate_stickman)

 
        if locate_stickman1 != None:
            print('I can see the target number 2')
            speak('I can see the target number 2')
            p.click(locate_stickman1)

        if locate_stickman2 != None:
            print('I can see it the target number 3')
            speak('I can see it the target number 3')
            p.click(locate_stickman2)

        if locate_stickman3 != None:
            print('I can see it the target number 4')
            speak('I can see it the target number 4')
            p.click(locate_stickman3)

        
        

locating()