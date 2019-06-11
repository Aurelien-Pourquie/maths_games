from tkinter import *
from classGrid import Grid
from classRules import Rules



def NewGrid():
	a = Grid(dimensionEntry.get(), rangeEntry.get(), rangeWindow.get())
	a.newGrid()

def showRules():
	a = Rules()

fen=Tk()
fen.title("A Complex Game of Life")

title=Label(fen, text="A Complex Game of Life")
title.pack(side="top", pady=(10,0), padx=60)

dimensionEntry=Entry(fen, bg="light blue")
dimensionEntry.insert(END, 'Dimension')
dimensionEntry.pack(side="left", pady=10, padx=(10,0))

rangeEntry=Entry(fen, bg="light blue")
rangeEntry.insert(END, 'Range')
rangeEntry.pack(side="left", pady=10, padx=(10,0))

rangeWindow=Entry(fen, bg="light blue")
rangeWindow.insert(END, 'Window size')
rangeWindow.pack(side="left", pady=10, padx=(10,0))

buttonGrid=Button(fen, text='New grid', command=NewGrid)
buttonGrid.pack(side="left", pady=10, padx=20)

buttonRules=Button(text="Rules", command=showRules, bg="dark grey", fg="red")
buttonRules.pack(side="right", pady=10, padx=(0,20))

fen.mainloop()
