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
liste_cible = []
################################################
# variables globales
nombre_mouvement_gen = 0
nombre_mouvement_right = 0
nombre_mouvement_left = 0
nombre_mouvement_up = 0
nombre_mouvement_down = 0

robot1_start_pos_X = 0
robot1_start_pos_Y = 0
robot2_start_pos_X = 0
robot2_start_pos_Y = 0
robot3_start_pos_X = 0
robot3_start_pos_Y = 0
robot4_start_pos_X = 0
robot4_start_pos_Y = 0


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
    global COTE, couleur_robot, x0, y0, a, b, robot1_start_pos_X, robot1_start_pos_Y
    x0, y0 = random.randint(0,LARGEUR//COTE - 1), random.randint(0,HAUTEUR//COTE - 1)
    robot1_start_pos_X, robot1_start_pos_Y = x0, y0
    a, b = x0 + 1, y0 + 1
    if a > x0 and b > y0:
        couleur = random.choice(couleur_robot)
        cercle1 = canvas.create_oval((x0*COTE, y0*COTE),(a*COTE, b*COTE),fill=couleur)
        couleur_robot.remove(couleur)
    print("robot1 :", x0, y0, a, b)
    return cercle1
def trace_robot2():
    global COTE, couleur_robot, x1, y1, a1, b1, robot2_start_pos_X, robot2_start_pos_Y
    x1, y1 = random.randint(0,LARGEUR//COTE - 1), random.randint(0,HAUTEUR//COTE - 1)
    robot2_start_pos_X, robot2_start_pos_Y = x1, y1
    a1, b1 = x1 + 1, y1 + 1
    if a1 > x1 and b1 > y1:
        couleur = random.choice(couleur_robot)
        cercle2 = canvas.create_oval((x1*COTE, y1*COTE),(a1*COTE, b1*COTE),fill=couleur)
        couleur_robot.remove(couleur)
    print("robot2 :", x1, y1, a1, b1)
    return cercle2
def trace_robot3():
    global COTE, couleur_robot, x2, y2, a2, b2, robot3_start_pos_X, robot3_start_pos_Y
    x2, y2 = random.randint(0,LARGEUR//COTE - 1), random.randint(0,HAUTEUR//COTE - 1)
    robot3_start_pos_X, robot3_start_pos_Y = x2, y2
    a2, b2 = x2 + 1, y2 + 1
    if a2 > x2 and b2 > y2:
        couleur = random.choice(couleur_robot)
        cercle3 = canvas.create_oval((x2*COTE, y2*COTE),(a2*COTE, b2*COTE),fill=couleur)
        couleur_robot.remove(couleur)
    print("robot3 :", x2, y2, a2, b2)
    
    return cercle3
def trace_robot4():
    global COTE, couleur_robot, x3, y3, a3, b3, robot4_start_pos_X, robot4_start_pos_Y
    x3, y3 = random.randint(0,LARGEUR//COTE - 1), random.randint(0,HAUTEUR//COTE - 1)
    robot4_start_pos_X, robot4_start_pos_Y = x3, y3
    a3, b3 = x3 + 1, y3 + 1
    if a3 > x3 and b3 > y3:
        couleur = random.choice(couleur_robot)
        cercle4 = canvas.create_oval((x3*COTE, y3*COTE),(a3*COTE, b3*COTE),fill=couleur)
        couleur_robot.remove(couleur)
    print("robot4 :", x3, y3, a3, b3)
    return cercle4
def trace_cible():
    global COTE, couleur_cible, liste_cible
    for i in range(1):
        x1, y1 = random.randint(0,LARGEUR//COTE - 1), random.randint(0,HAUTEUR//COTE - 1)
        x2, y2= x1 + 1, y1 +1
        if x2 > x1 and y2 > y1:
            couleur = random.choice(couleur_cible)
            carre = canvas.create_rectangle((x1*COTE, y1*COTE),(x2*COTE, y2*COTE),fill=couleur)
            couleur_cible.remove(couleur)
            liste_cible.append(carre)
    return[carre]

def clic(event):
    # position du pointeur de la souris
    global X, Y
    X = event.x / 30
    Y = event.y / 30
    print(X, Y)
    return True
def deplacement_robot(event): 
    # Sélection du robot à déplacer puis déplacement avec les touches directionnelles du clavier
    global X, Y
    X = event.x / 30
    Y = event.y / 30
    print(X, Y)
    touche = event.keysym
    if touche == "space":
        resetMap()
    
    if X >= x0 and X <= a :
            if Y >= y0 and Y <= b :
                if touche == "Up": # Déplacement du robot vers le haut
                    canvas.move(robot1, 0,-30)
                    compteur_deplacement("up")
                elif touche == "Down": # Déplacement du robot vers le bas
                    canvas.move(robot1, 0, 30)
                    compteur_deplacement("down")
                elif touche == "Right": # Déplacement du robot vers la droite
                    canvas.move(robot1, 30, 0)
                    compteur_deplacement("right")
                elif touche == "Left": # Déplacement du robot vers la gauche
                    canvas.move(robot1, -30, 0)
                    compteur_deplacement("left")
            print(touche, "robot1")
    elif X >= x1 and X <= a1 :
            if Y >= y1 and Y <= b1 :
                if touche == "Up": # Déplacement du robot vers le haut
                    canvas.move(robot2, 0,-30)
                    compteur_deplacement("up")
                elif touche == "Down": # Déplacement du robot vers le bas
                    canvas.move(robot2, 0, 30)
                    compteur_deplacement("down")
                elif touche == "Right": # Déplacement du robot vers la droite
                    canvas.move(robot2, 30, 0)
                    compteur_deplacement("right")
                elif touche == "Left": # Déplacement du robot vers la gauche
                    canvas.move(robot2, -30, 0)
                    compteur_deplacement("left")
            print(touche, "robot2")
    elif X >= x2 and X <= a2 :
            if Y >= y2 and Y <= b2 :
                if touche == "Up": # Déplacement du robot vers le haut
                    canvas.move(robot3, 0,-30)
                    compteur_deplacement("up")
                elif touche == "Down": # Déplacement du robot vers le bas
                    canvas.move(robot3, 0, 30)
                    compteur_deplacement("down")
                elif touche == "Right": # Déplacement du robot vers la droite
                    canvas.move(robot3, 30, 0)
                    compteur_deplacement("right")
                elif touche == "Left": # Déplacement du robot vers la gauche
                    canvas.move(robot3, -30, 0)
                    compteur_deplacement("left")
            print(touche, "robot3")
    elif X >= x3 and X <= a3 :
            if Y >= y3 and Y <= b3 :
                if touche == "Up": # Déplacement du robot vers le haut
                    canvas.move(robot4, 0,-30)
                    compteur_deplacement("up")
                elif touche == "Down": # Déplacement du robot vers le bas
                    canvas.move(robot4, 0, 30)
                    compteur_deplacement("down")
                elif touche == "Right": # Déplacement du robot vers la droite
                    canvas.move(robot4, 30, 0)
                    compteur_deplacement("right")
                elif touche == "Left": # Déplacement du robot vers la gauche
                    canvas.move(robot4, -30, 0)
                    compteur_deplacement("left")
            print(touche, "robot4")

def compteur_deplacement(direction):
    global nombre_mouvement_gen, nombre_mouvement_down, nombre_mouvement_up, nombre_mouvement_right, nombre_mouvement_left

    nombre_mouvement_gen += 1

    if direction == "right" :
        nombre_mouvement_right += 1
    if direction == "left" :
        nombre_mouvement_left += 1
    if direction == "up" :
        nombre_mouvement_up += 1
    if direction == "down" :
        nombre_mouvement_down += 1            

    print(nombre_mouvement_gen, "nombre déplacement general")
    print(nombre_mouvement_right, "nombre déplacement droite")
    print(nombre_mouvement_left, "nombre déplacement gauche")
    print(nombre_mouvement_up, "nombre déplacement haut")
    print(nombre_mouvement_down, "nombre déplacement bas")

def resetMap():
    print("reset")
    global robot1_start_pos_X, robot1_start_pos_Y, robot2_start_pos_X, robot2_start_pos_Y, robot3_start_pos_X, robot3_start_pos_Y, robot4_start_pos_X, robot4_start_pos_Y
    global x0, y0, x1, y1, x2, y2, x3, y3

    x0, y0 = robot1_start_pos_X, robot1_start_pos_Y
    x1, y1 = robot2_start_pos_X, robot2_start_pos_Y
    x2, y2 = robot3_start_pos_X, robot3_start_pos_Y
    x3, y3 = robot4_start_pos_X, robot4_start_pos_Y
    #canvas.moveto(robot2, robot2_start_pos_X, robot2_start_pos_Y)
    #canvas.moveto(robot1, robot1_start_pos_X, robot1_start_pos_Y)
    #canvas.moveto(robot3, robot3_start_pos_X, robot3_start_pos_Y)
    #canvas.moveto(robot4, robot4_start_pos_X, robot4_start_pos_Y)
    print(x0, y0)
    print(x1, y1)
    print(x2, y2)
    print(x3, y3)


# programme principale
racine = tk.Tk()
racine.title("Robot ricochet")
# création des widgets
canvas = tk.Canvas(racine, width = HAUTEUR, height = LARGEUR, bg = COULEUR_FOND)

# exécution des fonctions




quadrillage()

MurdeGauche = ((0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0),(1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0),(1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0),(1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0),(1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),(1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0),(1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0),(1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0),(1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0),(1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0),(1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0),(1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),(1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0),(1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0),(1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0),(1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0))
MurduHaut = ((0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),(0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0),(0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0),(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),(0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0),(0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0),(1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0),(0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0),(0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0),(0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0),(0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1),(0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0),(1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0),(0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0),(0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0),(0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0))



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

robot1 = trace_robot1()
robot2 = trace_robot2()
robot3 = trace_robot3()
robot4 = trace_robot4()
robot = [robot1, robot2, robot3, robot4]
cible = trace_cible()

#placement des widgets
canvas.grid()
canvas.bind("<Button-1>", deplacement_robot)
canvas.bind_all("<Up>", deplacement_robot)
canvas.bind_all("<Down>", deplacement_robot)
canvas.bind_all("<Right>", deplacement_robot)
canvas.bind_all("<Left>", deplacement_robot)
canvas.bind_all("<space>", deplacement_robot)


racine.mainloop()