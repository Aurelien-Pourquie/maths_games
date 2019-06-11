from tkinter import *
from random import randrange

class Grid:	
	
	def __init__(self) :
		self._range = 10 # chances of a cell being alive on init
		self.dimension=100 # square root of the number of cells
		self.win = 800 # dimension on screen
		self.case = self.win//self.dimension

		self.grilleInit = []
		self.newGrille = []

		self.grilleInit2 = []
		self.newGrille2 = []

		self.fen = Tk()
		self.fen.title("The Game of Life")		
		self.plateau=Canvas(self.fen,height=self.win,width=self.win)
		self.number=Canvas(self.fen)
		self.turns = Entry(self.fen, bg="light blue")
		self.nextTurn=Button(self.fen, text='Next turn', command=self.tourSuivant, bg="white")		
		self.manyTurns = Button(self.fen, text="Many turns", command=self.manyTurnsFunc, bg="white")

		self.nbOfTurns = 0
		self.nbOfTurnsLabel = Label(self.number, fg="red")		

	def newGrid(self):
				
		self.showEverything()		

	def showEverything(self):
		self.plateau.pack()
		self.nextTurn.pack()
		self.turns.pack(side="left", pady=5, padx=(360,5))
		self.manyTurns.pack(side="left")
		self.number.pack(side="bottom")
		self.nbOfTurnsLabel.pack()		

		self.createBoolGrid()
		self.createGrid()			

		##self.plateau.bind('<ButtonRelease>',self.clickCase)		

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

	"""def clickCase(self,event):
		i=event.x//self.case
		j=event.y//self.case		
		self.grilleInit[i][j]=True
		caseb=self.plateau.create_rectangle(i*self.case,j*self.case,(i+1)*self.case,(j+1)*self.case,fill="cyan", tag='recCyan')"""

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
		try:
			self.createGrid()
		except:
			pass