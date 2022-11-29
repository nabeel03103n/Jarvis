import pyautogui as p
from time import sleep
from pyttsx3 import speak

mango = "mango.png"
watermelon = 'watermelon.png'

while True:

    locate_mango = p.locateOnScreen(mango,confidence=0.8,grayscale=True)
    locate_watermelon = p.locateOnScreen(watermelon,confidence=0.8,grayscale=True)
# 9 11 12 - width
# 19 20 21 - height

    if locate_mango != None:
        p.moveTo(locate_mango)
        locate_mango = str(locate_mango)
        locate_mango = list(locate_mango)
        print(locate_mango," - mango")
        print(locate_mango[9],locate_mango[11],locate_mango[12])
        width = int(locate_mango[9],locate_mango[11],locate_mango[12])
        p.dragTo(width+50,locate_mango)

    if locate_watermelon != None:
        p.moveTo(locate_watermelon)
        locate_watermelon = str(locate_watermelon)
        print(locate_watermelon," - WaterMelon")
        # p.dragTo(locate_watermelon+50,locate_watermelon)

