################################################

# Groupe 1 BI TD1
# Princesse MOMO 
# Alexandra SCHMIDT
# Malak LALAMI
# Nolwenn CORIC
# Lilian JOANNET
# Tristan TOLENTINO
# https://github.com/uvsq22009244/projet_incendie

################################################
# import des modules

import tkinter as tk
import random 

################################################
# constantes

HAUTEUR = 256
LARGEUR = 256

COULEUR_FOND = "grey50"

################################################
# variables globales


################################################
# fonctions


# programme principale

racine = tk.Tk()
racine.title("Robot ricochet")

# création des widgets

canvas = tk.Canvas(racine, width = HAUTEUR, height = LARGEUR, bg = COULEUR_FOND)

canvas.grid()

racine.mainloop()