import pyautogui as p
from time import sleep
from pyttsx3 import speak


target = 'main.png'


while True:
    locate_main = p.locateOnScreen(target,confidence=0.8,grayscale=True)

    if locate_main != None:
        print("I can see it")
        speak("I can see it")
        p.click(locate_main)

    else:
        print("I'm not able to see it")
