from tkinter import *
from classGrid import Grid
from classRules import Rules

def NewGrid():
	a = Grid()
	a.newGrid()

def showRules():
	a = Rules()

size=Tk()
size.title("A Complex Game of Life")

title=Label(size, text="A Complex Game of Life")
title.pack(side="top", pady=(10,0), padx=60)

buttonGrid=Button(size, text='New grid', command=NewGrid)
buttonGrid.pack(side="left", pady=10, padx=20)

buttonRules=Button(text="Rules", command=showRules, bg="dark grey", fg="red")
buttonRules.pack(side="right", pady=10, padx=(0,20))

size.mainloop()
