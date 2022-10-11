import datetime
import time 
from tkinter import *

root = Tk()
root.title("Alarm Clock")
root.geometry("1000x700")


strTime = datetime.datetime.now().strftime("%H:%M:%S")    
Label(root,text=strTime).pack()


root.mainloop()
