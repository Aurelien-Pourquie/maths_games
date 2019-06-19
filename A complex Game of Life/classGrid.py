from tkinter import *
from random import randrange

class Grid:	
	
	def __init__(self,dimensionEntry, rangeEntry, windowEntry):
		try:
			if int(rangeEntry) > 0:
				self._range = int(rangeEntry) # chances of a cell being alive on init
			else:
				self._range = 2
		except:
			self._range = 2

		try:
			if int(dimensionEntry) > 0:
				self.dimension=int(dimensionEntry) # square root of the number of cells
			else:
				self.dimension=100 
		except:
			self.dimension=100 

		try:
			if int(windowEntry) >= 350:				
				self.win = int(windowEntry) # dimension on screen
			else:
				self.win = 800
		except:
			self.win = 800 

		self.case = self.win//self.dimension

		self.grilleInit = [] # The "blue" grid
		self.newGrille = []

		self.grilleInit2 = [] # The "orange" grid
		self.newGrille2 = []

		self.fen = Tk() # The Window
		self.fen.title("The Game of Life")		
		self.plateau=Canvas(self.fen,height=self.win,width=self.win, bg='white') # The Grid
		self.number=Canvas(self.fen) # The number of turns
		self.manyTurnsLine = Canvas(self.fen, highlightthickness=0) # Number of turns Entry + Many Turns Button
		self.nextTurnLine = Canvas(self.fen, highlightthickness=0) # Next Turn Button + Only Green Button
		self.turns = Entry(self.manyTurnsLine, bg="light blue") # Number of turns Entry
		self.nextTurn=Button(self.nextTurnLine, text='Next turn', command=self.tourSuivant, bg="white")
		self.onlyGreen=Button(self.nextTurnLine, text='Show green only', command=self.showGreen, bg='white')
		self.manyTurns = Button(self.manyTurnsLine, text="Many turns", command=self.manyTurnsFunc, bg="white") # Many Turns Button

		self.nbOfTurns = 0
		self.nbOfTurnsLabel = Label(self.number, fg="red")

		self.greenOnly = False

	def newGrid(self):
				
		self.showEverything()		

	def showEverything(self):
		self.plateau.pack()
		self.nextTurn.pack(side='left', padx=5, pady=(5,0))
		self.onlyGreen.pack(padx=5, pady=(5,0))
		self.nextTurnLine.pack()
		self.manyTurnsLine.pack()
		self.turns.pack(side='left', padx=5, pady=(5,0))
		self.manyTurns.pack(padx=5)
		self.number.pack() 
		self.nbOfTurnsLabel.pack()

		self.createBoolGrid()
		self.createGrid()			

	def showGreen(self):
		self.greenOnly = False if self.greenOnly else True
		
		if self.greenOnly:
			self.onlyGreen.configure(bg='green')
		else:
			self.onlyGreen.configure(bg='white')

		self.createGrid()

	def createBoolGrid(self):
		# 1
		for i in range(self.dimension):
			ligneInit = []
			for j in range(self.dimension):				
				if randrange(self._range) == 1:
					ligneInit.append(True)
				else:
					ligneInit.append(False)
			self.grilleInit.append(ligneInit)

		for i in range(self.dimension):
			ligneInit = []
			for j in range(self.dimension):				
					ligneInit.append(False)
			self.newGrille.append(ligneInit)

			# 2
		for i in range(self.dimension):
			ligneInit = []
			for j in range(self.dimension):				
				if randrange(self._range) == 1:
					ligneInit.append(True)
				else:
					ligneInit.append(False)
			self.grilleInit2.append(ligneInit)

		for i in range(self.dimension):
			ligneInit = []
			for j in range(self.dimension):				
					ligneInit.append(False)
			self.newGrille2.append(ligneInit)

	def createGrid(self):		
		self.nbOfTurnsLabel.config(text=("Turn = " + str(self.nbOfTurns)))

		if self.greenOnly:
			for i in range(self.dimension):
				for j in range(self.dimension):
					if self.grilleInit[i][j]!=True:
						self.plateau.create_rectangle(i*self.case,j*self.case,(i+1)*self.case,(j+1)*self.case,fill="white", tag='rec')
					else:
						self.plateau.create_rectangle(i*self.case,j*self.case,(i+1)*self.case,(j+1)*self.case,fill="white", tag='recCyan')

				for j in range(self.dimension):
					if self.grilleInit2[i][j]==True:
						if self.grilleInit[i][j]==True:
							self.plateau.create_rectangle(i*self.case,j*self.case,(i+1)*self.case,(j+1)*self.case,fill="green", tag='recGreen')
						else:
							self.plateau.create_rectangle(i*self.case,j*self.case,(i+1)*self.case,(j+1)*self.case,fill="white", tag='recOrange')

		else:
			for i in range(self.dimension):
				for j in range(self.dimension):
					if self.grilleInit[i][j]!=True:
						self.plateau.create_rectangle(i*self.case,j*self.case,(i+1)*self.case,(j+1)*self.case,fill="white", tag='rec')
					else:
						self.plateau.create_rectangle(i*self.case,j*self.case,(i+1)*self.case,(j+1)*self.case,fill="cyan", tag='recCyan')

				for j in range(self.dimension):
					if self.grilleInit2[i][j]==True:
						if self.grilleInit[i][j]==True:
							self.plateau.create_rectangle(i*self.case,j*self.case,(i+1)*self.case,(j+1)*self.case,fill="green", tag='recGreen')
						else:
							self.plateau.create_rectangle(i*self.case,j*self.case,(i+1)*self.case,(j+1)*self.case,fill="orange", tag='recOrange')	

	def clearPlateau(self):
			try:
				self.plateau.delete('rec')
				self.plateau.delete('recCyan')
				self.plateau.delete('recOrange')
				self.plateau.delete('recGreen')
			except:
				pass			

	def manyTurnsFunc(self):
		a = self.turns.get()		
		try:
			if (a != ""):
				for i in range(int(a)):
					self.tourSuivant()
					self.fen.update()
					self.fen.after(30)
		except:
			pass

	def tourSuivant(self):
		self.nbOfTurns = self.nbOfTurns + 1

		self.clearPlateau()

		### to be optimized

		for raw in range(self.dimension):
			for column in range(self.dimension):                        
				voisins = 0
    
			# En haut à gauche
				if raw != 0:
					if column != 0:
						try:
							if ((self.grilleInit[raw-1])[column-1]):
								voisins = voisins + 1
						except: 
							pass
            
			# En haut
					try:
						if ((self.grilleInit[raw-1])[column]):
							voisins = voisins + 1
					except: 
						pass
                
			# En haut à droite
					if column < self.dimension:
						try:
							if ((self.grilleInit[raw-1])[column+1]):
								voisins = voisins + 1
						except: 
							pass
                
				if column != 0:
			# A gauche
					try:
						if ((self.grilleInit[raw])[column-1]):
							voisins = voisins + 1
					except: 
						pass
                            
				if column < self.dimension:
			# A droite
					try:
						if ((self.grilleInit[raw])[column+1]):
							voisins = voisins + 1
					except: 
						pass
            
				if raw < self.dimension:
					if column != 0:
			# En bas à gauche
						try:
							if ((self.grilleInit[raw+1])[column-1]):
								voisins = voisins + 1
						except: 
							pass
                    
			# En bas
					try:
						if ((self.grilleInit[raw+1])[column]):
							voisins = voisins + 1
					except: 
						pass
        
					if column < self.dimension:
			# En bas à droite
						try:
							if ((self.grilleInit[raw+1])[column+1]):
								voisins = voisins + 1							
						except: 
							pass

			# on change la grille
					if self.grilleInit[raw][column] == False :				
						if voisins == 3:
							self.newGrille[raw][column] = True
					else:
						if (voisins == 2 or voisins == 3):
							self.newGrille[raw][column] = True
						else:
							self.newGrille[raw][column] = False
		for i in range (self.dimension):
			for j in range(self.dimension):
				self.grilleInit[i][j]=self.newGrille[i][j]

		######

		for raw in range(self.dimension):
			for column in range(self.dimension):                        
				voisins = 0
    
			# En haut à gauche
				if raw != 0:
					if column != 0:
						try:
							if ((self.grilleInit2[raw-1])[column-1]):
								voisins = voisins + 1
						except: 
							pass
            
			# En haut
					try:
						if ((self.grilleInit2[raw-1])[column]):
							voisins = voisins + 1
					except: 
						pass
                
			# En haut à droite
					if column < self.dimension:
						try:
							if ((self.grilleInit2[raw-1])[column+1]):
								voisins = voisins + 1
						except: 
							pass
                
				if column != 0:
			# A gauche
					try:
						if ((self.grilleInit2[raw])[column-1]):
							voisins = voisins + 1
					except: 
						pass
                            
				if column < self.dimension:
			# A droite
					try:
						if ((self.grilleInit2[raw])[column+1]):
							voisins = voisins + 1
					except: 
						pass
            
				if raw < self.dimension:
					if column != 0:
			# En bas à gauche
						try:
							if ((self.grilleInit2[raw+1])[column-1]):
								voisins = voisins + 1
						except: 
							pass
                    
			# En bas
					try:
						if ((self.grilleInit2[raw+1])[column]):
							voisins = voisins + 1
					except: 
						pass
        
					if column < self.dimension:
			# En bas à droite
						try:
							if ((self.grilleInit2[raw+1])[column+1]):
								voisins = voisins + 1							
						except: 
							pass

			# on change la grille
					if self.grilleInit2[raw][column] == False :				
						if voisins == 3:
							self.newGrille2[raw][column] = True
					else:
						if (voisins == 2 or voisins == 3):
							self.newGrille2[raw][column] = True
						else:
							self.newGrille2[raw][column] = False
		for i in range (self.dimension):
			for j in range(self.dimension):
				self.grilleInit2[i][j]=self.newGrille2[i][j]

		try:
			self.createGrid()
		except:
			pass