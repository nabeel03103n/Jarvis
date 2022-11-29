import pyautogui as p
import webbrowser
from time import sleep
import pyperclip

messages_on_screen = 'messages.png'
blue_dot = 'dot.png'
three_dots = 'threedots.png'
copy_btn = 'copy.png'
text_area = 'textarea.png'

webbrowser.open("https://instagram.com")
sleep(5)

p.click(p.locateOnScreen(messages_on_screen))
sleep(5)


check_dot = p.click(p.locateOnScreen(blue_dot))
if check_dot == None:

    exit

sleep(5)
p.moveTo(1066,868)

position_threedots = p.locateOnScreen(three_dots)
p.click(position_threedots)
# print(type(position_threedots))
position_threedots = list(position_threedots)
# print(type(position_threedots))
# print(position_threedots)
sleep(2)

width,height = position_threedots[0],position_threedots[1]

copying = p.click(width+175,height-48)
p.click(1216,993)
sleep(1)
p.typewrite(copying)

p.press('enter')

# def answering():

#     if content == "hi":
#         p.typewrite(content)
#         p.press("enter")





