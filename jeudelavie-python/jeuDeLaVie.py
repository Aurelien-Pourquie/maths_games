from tkinter import *

dimension = 200

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
				plateau.create_rectangle(i*5,j*5,(i+1)*5,(j+1)*5,fill="white", tag='rec')
			else:
				plateau.create_rectangle(i*5,j*5,(i+1)*5,(j+1)*5,fill="black", tag='recblack')

def clickCase(event):
	i=event.x//5
	j=event.y//5
	grilleInit[i][j]=True
	caseb=plateau.create_rectangle(i*5,j*5,(i+1)*5,(j+1)*5,fill="black", tag='recblack')

def clearPlateau():
        plateau.delete('rec')
        plateau.delete('recblack')

def tourSuivant():
        clearPlateau()
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

plateau=Canvas(fen,height=1000,width=1000)
plateau.pack()
createGrid()

plateau.bind('<ButtonRelease>',clickCase)

bouton1=Button(fen, text='Tour suivant', command=tourSuivant)
bouton1.pack()

fen.mainloop()
