from tkinter import *

def hello(event):
  print("Привет, программист!")

root = Tk()
root.title("Заголовок окна программы")
root.geometry("400x200")
but1 = Button(root)
but1["text"] = "Название кнопки"
but1.bind("<Button-1>",hello)

but1.pack()
root.mainloop()
input()
