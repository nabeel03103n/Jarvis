import pyautogui as p
import webbrowser
from time import sleep
from pyttsx3 import speak

# webbrowser.open("https://chrome://dino/")
tree = "tree.png"
tree2 = "tree2.png"

for i in range(3):
    sleep(i)
    print(f"Starting in {i} seconds")

while True:
    print("Tree 1",p.locateOnScreen(tree))

    print("Tree 2",p.locateOnScreen(tree2))