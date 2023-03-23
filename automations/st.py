import pyautogui as p
from time import sleep

db = {"Name":"Nabeel Ali Khan","Phone":"+917424810385","Email":"nabeel03103@gmail.com"}


for i in range(2):
    sleep(i)
    print(i)

p1 = p.locateOnScreen("name.png")
p1 = list(p1)

# print(p1)
# print(type(p1))
# print(p1[0])

width,height = p1[0],p1[1]

p.hotkey("ctrl","a")
p.typewrite(db["Name"])

p.click(width+100,height+50)

p.hotkey("ctrl","a")
p.typewrite(db["Phone"])

p.click(width+100,height+100)
p.hotkey("ctrl","a")
p.typewrite(db["Email"])