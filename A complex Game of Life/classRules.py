from tkinter import *

class Rules:

	def __init__(self):
		fen=Tk()	
		fen.title("Rules")	
		theRulesText=Text(fen, width=130, height=8)

		text = "- Any live cell with fewer than two live neighbours dies, as if by underpopulation."
		text = text + "\n- Any live cell with two or three live neighbours lives on to the next generation."
		text = text + "\n- Any live cell with more than three live neighbours dies, as if by overpopulation."
		text = text + "\n- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction."
		text = text + "\n\nHere we have a superposition of two grids following the preceding rules. When the living cells of both grids are superposed, they become a 'SuperCell', represented by a green color."
		theRulesText.insert(END, text)

		theRulesText.pack()		