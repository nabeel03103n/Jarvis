from tkinter import *
import random
from turtle import clear
from pyttsx3 import speak
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import pyautogui


font = "Lucida 10"
fontBtn = "Lucida 10 bold"

def submit(events):
    speak(TextArea.get(1.0,END))
def submit1():
    speak(TextArea.get(1.0,END))

def clear(events):
    TextArea.delete(1.0,END)
def clear1():
    TextArea.delete(1.0,END)

def help():
    showinfo("Speaker",'''
1. Press Enter for Submit
2. Press Esc for Clear''')

def open1():
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    TextArea.delete(1.0, END)

    f = open(file,"r")
    TextArea.insert(1.0,f.read())
    f.close()
    pyautogui.press("enter")

root = Tk()
root.title("Nabeel's Typing Tutor")
root.geometry("700x500")
root.minsize(700,500)
root.maxsize(700,500)
root.configure(bg="brown")

MenuBar = Menu(root)
MenuBar.add_command(label="Open",command=open1)
MenuBar.add_command(label="Help",command=help)

f1 = Frame(root,bg="antiquewhite")
f1.pack()


TextArea = Text(f1,height=17,font=font)
TextArea.pack(pady=10)

btn1 = Button(f1,text="Submit",font=fontBtn,bg="black",command=submit1,fg="white")
btn1.pack(ipadx=300)

btn2 = Button(f1,text="Clear",font=fontBtn,bg="red",command=clear1)
btn2.pack(ipadx=300)

root.bind("<Return>",submit)
root.bind("<Escape>",clear)


root.config(menu=MenuBar)

root.mainloop()

