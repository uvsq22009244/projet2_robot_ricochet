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
couleur_robot = ["yellow", "red", "blue", "green"]
couleur_cible = ["yellow", "red", "blue", "green"]
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

def trace_robot1():
    global COTE, couleur_robot, x0, y0, a, b, element_robot
    x0, y0 = random.randint(0,LARGEUR//COTE - 1), random.randint(0,HAUTEUR//COTE - 1)
    a, b = x0 + 1, y0 + 1
    if a > x0 and b > y0:
        couleur = random.choice(couleur_robot)
        cercle1 = canvas.create_oval((x0*COTE, y0*COTE),(a*COTE, b*COTE),fill=couleur)
        couleur_robot.remove(couleur)
    
    return cercle1

def trace_robot2():
    global COTE, couleur_robot, x1, y1, a1, b1
    x1, y1 = random.randint(0,LARGEUR//COTE - 1), random.randint(0,HAUTEUR//COTE - 1)
    a1, b1 = x1 + 1, y1 + 1
    if a1 > x1 and b1 > y1:
        couleur = random.choice(couleur_robot)
        cercle2 = canvas.create_oval((x1*COTE, y1*COTE),(a1*COTE, b1*COTE),fill=couleur)
        couleur_robot.remove(couleur)
    
    return cercle2

def trace_cible():
    global COTE, couleur_cible
    for i in range(4):
        x1, y1 = random.randint(0,LARGEUR//COTE - 1), random.randint(0,HAUTEUR//COTE - 1)
        x2, y2= x1 + 1, y1 +1
        if x2 > x1 and y2 > y1:
            couleur = random.choice(couleur_cible)
            carre = canvas.create_rectangle((x1*COTE, y1*COTE),(x2*COTE, y2*COTE),fill=couleur)
            couleur_cible.remove(couleur)

    return[carre]

def trace_mur():
    global COTE
    mur_horizontal_haut = canvas.create_line((0,0), (2*COTE,0), width = 10, fill = "black")
    mur_horizontal_bas = canvas.create_line((2*COTE, 2*COTE),(0, 2*COTE), width = 10, fill = "black")
    mur_vertical_droite = canvas.create_line((2*COTE, 0),(2*COTE, 2*COTE), width = 10, fill = "black")
    mur_vertical_gauche = canvas.create_line((0,2*COTE), (0,0), width = 10, fill = "black")

"""def coord_robot(event):
    print(event.x, event.y)
    return coord_robot"""

def deplacement_robot1(event): 
    # Déplacement du robot1 avec les touches directionnelles du clavier
    global robot1
    touche = event.keysym
    print(touche, robot1)
    if touche == "Up": # Déplacement du robot vers le haut
        canvas.move(robot1, 0,-30)
    elif touche == "Down": # Déplacement du robot vers le bas
        canvas.move(robot1, 0, 30)
    elif touche == "Right": # Déplacement du robot vers la droite
        canvas.move(robot1, 30, 0)
    elif touche == "Left": # Déplacement du robot vers la gauche
        canvas.move(robot1, -30, 0)

def deplacement_robot2(event): 
    # Déplacement du robot avec les touches directionnelles du clavier
    global robot2
    touche = event.keysym
    print(touche, "robot2")
    if touche == "Up": # Déplacement du robot vers le haut
        canvas.move(robot2, 0,-30)
    elif touche == "Down": # Déplacement du robot vers le bas
        canvas.move(robot2, 0, 30)
    elif touche == "Right": # Déplacement du robot vers la droite
        canvas.move(robot2, 30, 0)
    elif touche == "Left": # Déplacement du robot vers la gauche
        canvas.move(robot2, -30, 0)

def compteur_deplacement():
    pass
# programme principale

racine = tk.Tk()
racine.title("Robot ricochet")

# création des widgets

canvas = tk.Canvas(racine, width = HAUTEUR, height = LARGEUR, bg = COULEUR_FOND)

# exécution des fonctions

quadrillage()
robot1 = trace_robot1()
robot2 = trace_robot2()
robot = [robot1, robot2]
cible = trace_cible()
trace_mur()

#placement des widgets
canvas.grid()

#canvas.bind("<Button-1>", coord_robot)
canvas.bind_all("<Up>", deplacement_robot1)
canvas.bind_all("<Down>", deplacement_robot1)
canvas.bind_all("<Right>", deplacement_robot1)
canvas.bind_all("<Left>", deplacement_robot1)

canvas.bind_all("<Up>", deplacement_robot2)
canvas.bind_all("<Down>", deplacement_robot2)
canvas.bind_all("<Right>", deplacement_robot2)
canvas.bind_all("<Left>", deplacement_robot2)

racine.mainloop()