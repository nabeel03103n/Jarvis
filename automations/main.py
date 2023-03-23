from tkinter import *
import pyautogui as p

def submit():
    # with open("db.txt","a+")as f:
    #     f.write(e1.get()+"\n")
    #     f.write(e2.get()+"\n")
    #     f.write(e3.get()+"\n")
    pass

db = {"Name":"Nabeel Ali Khan","Phone":"+917424810385","Email":"nabeel03103@gmail.com"}

root =  Tk()
root.geometry("444x444")
root.title("Automation")

Label(root,text="Name: ",font='lucida').grid(row=0,column=0)
e1 = Entry(root)
e1.insert(0,"Enter your name")
e1.grid(row=0,column=1)

Label(root,text="Phone: ",font='lucida').grid()
e2 = Entry(root)
e2.insert(0,"Enter your Phone number")
e2.grid(row=1,column=1)

Label(root,text="Email: ",font='lucida').grid()
e3 = Entry(root)
e3.grid(row=2,column=1)

btn = Button(root,text="Submit",command=submit)
btn.grid()




root.mainloop()