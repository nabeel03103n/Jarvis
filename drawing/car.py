import os
from turtle import left 
import pyautogui as p 
from time import sleep

circle = 605,95
rect = 629,96
eraser = 346,147
line = 535,92

def draw():
    os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint.lnk")
    sleep(1)
    print(p.position())

    p.click(circle)
    p.moveTo(394,774)
    p.dragTo(394,774,button='left')
    p.dragTo(546,643,0.5,button='left')

    p.moveTo(1222,770)
    p.dragTo(1222,770,button='left')
    p.dragTo(1063,640,0.5,button='left')

    p.click(rect)
    p.moveTo(1316,420)
    p.dragTo(1316,420,button='left')
    p.dragTo(331,708,0.5,button='left')

    p.click(eraser)
    p.moveTo(400,707)
    p.dragTo(400,707,button='left')
    p.dragTo(545,708,0.5,button='left')

    p.moveTo(1070,708)
    p.dragTo(1070,708,button='left')
    p.dragTo(1220,709,0.5,button='left')

    with p.hold("ctrl"):
        p.press("a")

    p.moveTo(795,547)
    p.dragTo(837,782,0.5,button='left')
    p.press('esc')
    p.click(line)

    p.moveTo(1083,628)
    p.dragTo(947,487,0.5,button='left')
    p.click(1000,487)
    p.click(947,487)
    p.moveTo(947,487)
    p.dragTo(373,487,0.5,button='left')
    p.moveTo(373,487)
    p.dragTo(369,629,0.5,button='left')

    p.moveTo(1085,631)
    p.dragTo(1085,917,0.5,button='left')
    p.moveTo(774,631)
    p.dragTo(774,918,0.5,button='left')
    p.click(rect)
    p.moveTo(796,717)
    p.dragTo(883,685,0.5,button='left')
    p.click(520,630)
    p.dragTo(519,854,0.5,button='left')

    p.click(eraser)
    p.click(574,919)

draw()