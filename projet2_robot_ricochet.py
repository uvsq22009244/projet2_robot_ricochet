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

HAUTEUR = 480
LARGEUR = 480
COULEUR_FOND = "grey50"
COTE = 30
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


def dessin_robot():
    
    pass


def dessin_cible():
    
    pass


def deplacement_robot():
    
    pass

def compteur_deplacement():
    
    pass

#programme principal

racine = tk.Tk()
racine.title("Robot ricochet")

#création des widgets

canvas = tk.Canvas(racine, width = HAUTEUR,
                           height = LARGEUR, 
                           bg = COULEUR_FOND)


quadrillage()
canvas.create_oval(90,90,120,120,fill="blue")
canvas.create_oval(200,200,230,230,fill="red")
canvas.create_oval(300,300,330,330,fill="green")
canvas.create_oval(400,400,430,430,fill="yellow")
canvas.create_rectangle(250,250,280,280 ,fill="blue")
canvas.create_rectangle(60,60,90,90,fill="red")
canvas.create_rectangle(160,160,190,190,fill="green")
canvas.create_rectangle(30,30,60,60,fill="yellow")
#il faut faire une fonction pour qu'ils soient placés au hasard 

# placement des widgets

canvas.grid()
racine.mainloop()
