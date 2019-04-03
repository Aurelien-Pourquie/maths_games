from tkinter import *
import sys
import math
dimension = 20

grilleInit = []
newGrid = []

for i in range(dimension):
	ligneInit = []
	for j in range(dimension):
		ligneInit.append(False)
	grilleInit.append(ligneInit)

for i in range(dimension):
	ligneInit = []
	for j in range(dimension):
		ligneInit.append(False)
	newGrid.append(ligneInit)

def createGrid():
	for i in range(dimension):
		for j in range(dimension):
			if grilleInit[i][j]!=True:
				plateau.create_rectangle(i*40,j*40,(i+1)*40,(j+1)*40,fill="white")
			else:
				plateau.create_rectangle(i*40,j*40,(i+1)*40,(j+1)*40,fill="black")

def clicCase(event):
	i=event.x//40
	j=event.y//40	
	grilleInit[i][j]=True
	coord['text']=str(i)+','+str(j)+','+str(grilleInit[i][j])
	caseb=plateau.create_rectangle(i*40,j*40,(i*40+40),(j*40+40),fill="black")

def tourSuivant():

	for raw in range(dimension):
		for column in range(dimension):
			
			voisins = 0
        
	        # En haut à gauche
			if raw != 0:
				if column != 0:
					try:
						if ((grilleInit[raw-1])[column-1]):
							voisins = voisins + 1
					except: 
						pass
	        
	            # En haut
				try:
					if ((grilleInit[raw-1])[column]):
						voisins = voisins + 1
				except: 
					pass
	            
	            # En haut à droite
				if column < dimension:
					try:
						if ((grilleInit[raw-1])[column+1]):
							voisins = voisins + 1
					except: 
						pass
	            
			if column != 0:
	            # A gauche
				try:
					if ((grilleInit[raw])[column-1]):
						voisins = voisins + 1
				except: 
					pass
			if column < dimension:
	        # A droite
				try:
					if ((grilleInit[raw])[column+1]):
						voisins = voisins + 1
				except: 
					pass
	        
			if raw < dimension:
				if column != 0:
	                # En bas à gauche
					try:
						if ((grilleInit[raw+1])[column-1]):
							voisins = voisins + 1
					except: 
						pass
	                
	            # En bas
				try:
					if ((grilleInit[raw+1])[column]):
						voisins = voisins + 1
				except: 
					pass
	            
				if column < dimension:
	                # En bas à droite
					try:
						if ((grilleInit[raw+1])[column+1]):
							voisins = voisins + 1							
					except: 
						pass

				# on change la grille
				if grilleInit[raw][column] == False :				
					if voisins == 3:
						newGrid[raw][column] = True
				else:
					if (voisins == 2 or voisins == 3):
						newGrid[raw][column] = True
					else:
						newGrid[raw][column] = False
	for i in range (dimension):
		for j in range(dimension):
			grilleInit[i][j]=newGrid[i][j]
	createGrid()

fen = Tk()
fen.title("Le jeu de la vie")

plateau=Canvas(fen,height=800,width=800)
plateau.pack()
createGrid()

plateau.bind('<ButtonRelease>',clicCase)

bouton1=Button(fen, text='Tour suivant', command=tourSuivant)
bouton1.pack()

coord=Label(fen)
coord.pack(pady='10px')

fen.mainloop()