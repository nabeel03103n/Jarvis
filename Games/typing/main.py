import os 
from time import sleep
import pyautogui as p

os.startfile("C:\\Users\\Metro\\OneDrive\\Desktop\\Kiran's Typing Tutor.lnk")
sleep(3)
# p.hotkey("alt","tab")
p.click(p.locateOnScreen("ok.png"))

sleep(1)

p.click(1458,285)
p.typewrite('nabeel')
p.press('enter')
sleep(1)

p.hotkey("ctrl","t")
p.click(923,196)
p.hotkey('ctrl','a')
p.hotkey('ctrl','c')
sleep(2)
p.click(903,629)
sleep(1)
p.keyDown("ctrl")
p.press("v")
p.keyDown("ctrl")