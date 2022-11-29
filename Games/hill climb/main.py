import pyautogui as p
import pydirectinput as pd
from time import sleep
from pyttsx3 import speak

diamond = 'diamond.png'
car_up = 'car_up.png'
coin25 = 'coin_25.png'

while True:

    locate_diamond = p.locateOnScreen(diamond,confidence=0.8,grayscale=True)
    locate_carup = p.locateOnScreen(car_up,confidence=0.8,grayscale=True)
    locate_coin25 = p.locateOnScreen(coin25,confidence=0.7,grayscale=True)

    if locate_diamond != None:
        pd.keyUp('left')
        pd.keyDown('right')
        speak("Diamond Spotted")

    if locate_carup != None:
        pd.keyUp('right')
        pd.keyDown('left')

    if locate_coin25 != None:
        pd.keyUp('right')
        pd.keyDown('left')

    else:
        speak("Nothing")