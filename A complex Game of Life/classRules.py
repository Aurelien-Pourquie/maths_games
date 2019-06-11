from tkinter import *

class Rules:

	def __init__(self):
		fen=Tk()	
		fen.title("Rules")	
		theRulesText=Text(fen, width=100, height=5)
		theRulesText.insert(END, "- Any live cell with fewer than two live neighbours dies, as if by underpopulation.\n- Any live cell with two or three live neighbours lives on to the next generation.\n- Any live cell with more than three live neighbours dies, as if by overpopulation.\n- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.")

		theRulesText.pack()		