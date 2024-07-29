# `ShapeStyle/background` shape style.
from tkinter import *

root = Tk()
canvas = Canvas(root, width=200, height=200)
canvas.pack()

# Creating a circle with a blue background
canvas.create_oval(50, 50, 150, 150, fill='blue')

root.mainloop()
