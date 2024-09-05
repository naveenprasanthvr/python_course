import tkinter as tk
from tkinter import ttk
import turtle as t



t.lt(90)
t.speed(0)

count = 0



def forward():
    t.fd(50)
    
def back():
    t.bk(50)
    
def right():
    t.rt(90)
    
def left():
    t.lt(90)
    
def pen():
    global count
    count+=1
    if (count%2==1):
        t.penup()
        lift.config(text="Drop Pen",bg='red')
    elif (count%2==0):
        t.pendown()
        lift.config(text="Lift Pen",bg='green')
        

colr = "cyan"

root = tk.Tk()
root.resizable(False,False)



fbut = tk.Button(root,bg=colr,text="Forward",command=forward)
fbut.grid(row=0,column=1)


bbut = tk.Button(root,bg=colr,text="Backward",command=back)
bbut.grid(row=2,column=1)


lbut = tk.Button(root,bg=colr,text="Turn Left",command=left)
lbut.grid(row=1,column=0)


rbut = tk.Button(root,bg=colr,text="Turn Right",command=right)
rbut.grid(row=1,column=2)


lift = tk.Button(root,bg="green",fg='white',text="Lift Pen",command=pen)
lift.grid(row=1,column=1)


t.done()
root.mainloop()