from tkinter import *  
from tkinter import ttk, Frame, Label  
from turtle import*
import random
t1 = ("88")
t2 = ("99")
t3 = ("87")

def clicked():
    op1.configure(text=random.random())

def clicked1():
    op3.configure(text=random.uniform(1, 99999999))

def clicked2():
    #treugolnik
    forward(65)
    left(103)
    forward(65)
    left(130)
    forward(78)
def clicked3():
    #kvadrat
    forward(60)
    right(90)
    forward(60)
    right(90)
    forward(60)
    right(90)
    forward(60)
def clicked4():
    #flazok
    forward(60)
    right(100)
    forward(25)
    right(145)
    forward(29)
    left(69)
    forward(45)
    
    
 
window = Tk()  
window.title("РАНДОМАЙЗЕР и генератор фигур!")  
window.geometry('450x250')  
tab_control = ttk.Notebook(window)  
tab1 = ttk.Frame(tab_control)  
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='цифры')
tab_control.add(tab2, text='фигуры')
op=Button(tab1, text="Нажмите чтобы получить цифру с плавующей точкой!", bg="blue", fg="black", command=clicked, padx="15", pady="9", font="15")
op.pack(side=BOTTOM) 
op1 = Label(tab1, text="______________", padx="15", pady="8", font="15")
op1.pack(side=BOTTOM) 
op2=Button(tab1,text="Нажмите чтобы получить цифру без плавующей точки!", bg="green", fg="black", command=clicked1, padx="15", pady="7", font="15")
op2.pack(side=BOTTOM)
op3 = Label(tab1, text="______________", padx="15", pady="6", font="15")
op3.pack(side=BOTTOM) 
op5 = Label(tab1, text="Эта программа для создания псевдослучайных чисел!", padx="15", pady="10", font="15")
op5.pack(side=BOTTOM)
op5 = Label(tab2, text="Эта часть программы для генерации фигур!", padx="15", pady="10", font="15")
op5.pack(side=TOP)
op6=Button(tab2, text="треугольник", bg="red", fg="black", command=clicked2, padx="15", pady="9", font="15")
op6.pack(side=BOTTOM)
op7=Button(tab2, text="квадрат", bg="blue", fg="black", command=clicked3, padx="15", pady="9", font="15")
op7.pack(side=RIGHT)
op8=Button(tab2, text="флажок", bg="green", fg="black", command=clicked4, padx="15", pady="9", font="15")
op8.pack(side=LEFT)
tab_control.pack(expand=1, fill='both')
window.mainloop()

