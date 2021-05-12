import random as rd

################################################

# Groupe 1 BI TD1
# Princesse MOMO 
# Alexandra SCHMIDT
# Malak LALAMI
# Nolwenn CORIC
# Lilian JOANNET
# Tristan TOLENTINO
# https://github.com/uvsq22009244/projet2_robot_ricochet

################################################
# import des modules

import tkinter as tk
import random 

################################################
# constantes

HAUTEUR = 640
LARGEUR = 640
COULEUR_FOND = "grey50"
COTE = 40
COULEUR_QUADR = "grey60"
################################################
# variables globales


################################################
# fonctions

def quadrillage():
    """Dessine un quadrillage dans le canevas avec des carrés de côté COTE"""
    y = 0
    while y <= HAUTEUR:
        canvas.create_line((0, y), (LARGEUR, y), fill=COULEUR_QUADR)
        y += COTE
    i = 0
    while i * COTE <= LARGEUR:
        x = i * COTE
        canvas.create_line((x, 0), (x, HAUTEUR), fill=COULEUR_QUADR)
        i += 1

# programme principal





racine = tk.Tk()
racine.title("Robot ricochet")

# création des widgets

canvas = tk.Canvas(racine, width = HAUTEUR, height = LARGEUR, bg = COULEUR_FOND)
#canvas.create_oval(racine, )
#cercle = canvas.create_oval((10, 10), (30, 30), fill="red", width=5, outline="red")

fic = open("test.txt","w")
#fic.write("hello")

def mur():
    if n == 1:
        canvas.create_line((0,100),(20,600), fill = "red")

global x
global n
x = 0
n = 0

for i in range(15):
    
    if x < 3 :
        n = rd.randint(0,1)
        fic.write(str(n))
        x = x + 1
    if x == 3:
        n = rd.randint(0,1)
        fic.write(str(n)+ "\n")
        x = 0

fic.close()

fic = open("notes.txt", "r")
for ligne in fic:
    print(ligne)
fic.close()


res = 0
fic = open("notes.txt", "r")

for ligne in fic:
    v = ligne.split()[0]

fic.close()
print("La somme des notes vaut", res)





        
        


L = [[0]*4 for i in range(4)]
print(L)

#canvas.create_line((0,0),(0,200),fill = "blue", width = 20)
#canvas.create_line((400,0),(400,200),fill = "blue", width = 20)
quadrillage()


#création des murs du plateau de jeu

MurdeGauche = ((1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0),(1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0),(1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0),(1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0),(1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),(1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0),(1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0),(1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0),(1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0),(1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0),(1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0),(1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),(1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0),(1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0),(1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0),(1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0))

Gtout = ((1,0,0,0),(0,0,1,1),(1,0,0,1),(0,0,1,0),(1,1,0,0),(0,1,0,0),(0,0,0,0),(0,0,1,0),(1,0,0,0))

G = ((1,0,1),(0,1,0),(0,0,1))
H = ((0,0,0),(0,1,1),(0,0,0))

MurduHaut = ((0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),(0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0),(0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0),(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),(0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0),(0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0),(1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0),(0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0),(0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0),(0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0),(0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1),(0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0),(1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0),(0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0),(0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0),(0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0))



def murgauche():
    pass


for i in range(len(MurdeGauche)):
    for j in range(len(MurdeGauche[i])):
        if MurdeGauche[i][j] == 1 :
            canvas.create_line((j*COTE,i*COTE),(j*COTE,(i+1)*COTE),fill = "black", width = 10)

for i in range(len(MurduHaut)):
    for j in range(len(MurduHaut[i])):
        if MurduHaut[i][j] == 1 :
            canvas.create_line((j*COTE,i*COTE),((j+1)*COTE,i*COTE),fill = "black", width = 10)

#murs extérieurs
canvas.create_line((0,0),(0,HAUTEUR),fill = "black", width = 10)
canvas.create_line((0,0),(LARGEUR,0),fill = "black", width = 10)
canvas.create_line((LARGEUR,0),(LARGEUR,HAUTEUR),fill = "black", width = 10)
canvas.create_line((0,HAUTEUR),(LARGEUR,HAUTEUR),fill = "black", width = 10)

#mur en carré au centre
canvas.create_line((7*COTE,7*COTE),(9*COTE,7*COTE),fill = "black", width = 10)
canvas.create_line((7*COTE,7*COTE),(7*COTE,9*COTE),fill = "black", width = 10)
canvas.create_line((7*COTE,9*COTE),(9*COTE,9*COTE),fill = "black", width = 10)
canvas.create_line((9*COTE,9*COTE),(9*COTE,7*COTE),fill = "black", width = 10)

#ou peut être que un rectangle, car plus simple?
canvas.create_rectangle((7*COTE,7*COTE),(9*COTE,9*COTE),fill = "white", width = 10)


#placement des widgets
canvas.grid()




racine.mainloop()




