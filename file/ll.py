from tkinter import *
import random

op=1
op1=2
op2=3
op3=4
op4=5
op5=6
op6=7
op7=8
op8=9
iop=11
iop1=12
iop2=13
iop3=14
iop4=15
iop5=16
iop6=17
iop7=18
iop8=19











def hello(event):
    print(random.random())

u = Tk()
u.title("РАНДОМАЙЗЕР!")
u.geometry("600x300")
op=Button(u)
op["text"] = "нажмите чтобы получить цифру!"
op.pack()
op.bind("<Button-1>",hello)

op.pack()
u.mainloop()
input()

