import pyautogui as p
import webbrowser
from time import sleep
import pyperclip
import os
from googlesearch import search

messages_on_screen = 'messages.png'
blue_dot = 'dot.png'
three_dots = 'threedots.png'
copy_btn = 'copy.png'
text_area = 'textarea.png'
three_dots2 = 'threedots2.png'

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
position_threedots2 = p.locateOnScreen(three_dots2)
try:
    p.click(position_threedots)
    # print(type(position_threedots))
    position_threedots = list(position_threedots)

# print(type(position_threedots))
# print(position_threedots)

except:
    p.click(position_threedots2)
    position_threedots = list(position_threedots2)


sleep(2)

width,height = position_threedots[0],position_threedots[1]

p.click(width+175,height-48)
p.click(1216,993)



path = "db.txt"

with open(path,'w')as f:
    f.write(" ")

fd = os.open(path, os.O_WRONLY)
s = pyperclip.paste()
line = str.encode(s).lower()
    

os.write(fd, line)
os.close(fd)
print("File descriptor closed successfully")

with open("db.txt")as f:
    # p.typewrite(f.read())
    f = f.read().lower()
    
    if f == "hi":
        p.typewrite("Hello I'm Jarvis please tell me how may I help you")

    elif f == "hello":
        p.typewrite("Hello I'm Jarvis please tell me how may i help you")


    elif "my name is" in f:
        f = f.replace("my name is"," ")
        p.typewrite(f"Hello {f.capitalize()}. I'm Jarvis")

    elif "nabeel" in f:
        p.typewrite("My master Nabeel is busy with some work please tell me how may I help you, I'm Jarvis")


    else:
        j = ""
        for j in search(f, tld="co.in", num=1, stop=1, pause=1):
                print(j)
                p.typewrite("Here are the results")
                p.press('enter')
                p.typewrite(j)

p.press('enter')



# p.keyDown('ctrl')
# p.press('v')
# p.keyUp('ctrl')
# sleep(0.5)

# # p.doubleClick(1216,993)
# p.hotkey('ctrl','a')
# p.hotkey('ctrl','x')

# os.startfile("db.txt")


# def answering():

#     if content == "hi":
#         p.typewrite(content)
#         p.press("enter")





