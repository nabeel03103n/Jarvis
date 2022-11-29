import pyautogui as p
from time import sleep
from pyttsx3 import speak
import pydirectinput as pd

enemy = 'enemy.png'

while True:
    locate_enemy = p.locateOnScreen(enemy,confidence=0.8,grayscale=False)

    if locate_enemy != None:
        speak("yes")
        print("yes")
    else:
        p.hold('l')
        print("NO")
        speak("NO")
