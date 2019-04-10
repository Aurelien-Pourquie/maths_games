from tkinter import *
from classGrid import Grid
from classRules import Rules

def sizeS():
	a = Grid()
	a.newGrid("S")

def sizeM():
	a = Grid()
	a.newGrid("M")

def sizeL():
	a = Grid()
	a.newGrid("L")

def sizeXL():
	a = Grid()
	a.newGrid("XL")

def showRules():
	a = Rules()

size=Tk()
size.title("The Game of Life")

choice=Label(size, text="Please choose a size for the grid")
choice.pack(side="top", pady=10, padx=60)
buttonS=Button(size, text='S', command=sizeS)
buttonS.pack(side="left", pady=20, padx=20)
buttonM=Button(size, text='M', command=sizeM)
buttonM.pack(side="left", pady=20, padx=20)
buttonL=Button(size, text='L', command=sizeL)
buttonL.pack(side="left", pady=20, padx=20)
buttonXL=Button(size, text='XL', command=sizeXL)
buttonXL.pack(side="left", pady=20, padx=20)

buttonRules=Button(text="Rules", command=showRules, bg="dark grey", fg="red")
buttonRules.pack(side="left", pady=20, padx=(20,10))

size.mainloop()
