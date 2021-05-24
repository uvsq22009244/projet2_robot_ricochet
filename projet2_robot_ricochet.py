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

score=0

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
    global COTE, couleur_robot, x0, y0, a, b
    global robot1_start_pos_X, robot1_start_pos_Y
    x0=7
    y0=7
    while(x0==7 and y0==7) or (x0==8 and y0==7) or (x0==7 and y0==8) or (x0==8 and y0==8 ):
        x0, y0 = random.randint(0,LARGEUR//COTE - 1), random.randint(0,HAUTEUR//COTE - 1)
    a, b = x0 + 1, y0 + 1
    robot1_start_pos_X, robot1_start_pos_Y = x0, y0
    couleur = "red"
    cercle1 = canvas.create_oval((x0*COTE, y0*COTE),(a*COTE, b*COTE),fill=couleur)
    couleur_robot.remove(couleur)
    print("robot1 :", x0, y0, a, b)
    return cercle1

def trace_robot2():
    global COTE, couleur_robot, x1, y1, a1, b1
    global robot2_start_pos_X, robot2_start_pos_Y
    x1=7
    y1=7
    while(x1==7 and y1==7) or (x1==8 and y1==7) or (x1==7 and y1==8) or (x1==8 and y1==8 ):
        x1, y1 = random.randint(0,LARGEUR//COTE - 1), random.randint(0,HAUTEUR//COTE - 1)
    a1, b1 = x1 + 1, y1 + 1
    robot2_start_pos_X, robot2_start_pos_Y = x1, y1
    couleur = "blue"
    cercle2 = canvas.create_oval((x1*COTE, y1*COTE),(a1*COTE, b1*COTE),fill=couleur)
    couleur_robot.remove(couleur)
    print("robot2 :", x1, y1, a1, b1)
    return cercle2

def trace_robot3():
    global COTE, couleur_robot, x2, y2, a2, b2
    global robot3_start_pos_X, robot3_start_pos_Y
    x2=7
    y2=7
    while(x2==7 and y2==7) or (x2==8 and y2==7) or (x2==7 and y2==8) or (x2==8 and y2==8 ):
        x2, y2 = random.randint(0,LARGEUR//COTE - 1), random.randint(0,HAUTEUR//COTE - 1)
    a2, b2 = x2 + 1, y2 + 1
    robot3_start_pos_X, robot3_start_pos_Y = x2, y2 
    couleur = "yellow"
    cercle3 = canvas.create_oval((x2*COTE, y2*COTE),(a2*COTE, b2*COTE),fill=couleur)
    couleur_robot.remove(couleur)
    print("robot3 :", x2, y2, a2, b2)
    return cercle3

def trace_robot4():
    global COTE, couleur_robot, x3, y3, a3, b3
    global robot4_start_pos_X, robot4_start_pos_Y
    x3=7
    y3=7
    while(x3==7 and y3==7) or (x3==8 and y3==7) or (x3==7 and y3==8) or (x3==8 and y3==8 ):
        x3, y3 = random.randint(0,LARGEUR//COTE - 1), random.randint(0,HAUTEUR//COTE - 1)
    a3, b3 = x3 + 1, y3 + 1
    robot4_start_pos_X, robot4_start_pos_Y = x3, y3
    couleur = random.choice(couleur_robot)
    cercle4 = canvas.create_oval((x3*COTE, y3*COTE),(a3*COTE, b3*COTE),fill=couleur)
    couleur_robot.remove(couleur)
    print("robot4 :", x3, y3, a3, b3)
    return cercle4

def trace_cible():
    global COTE, couleur_cible, liste_cible, x_cible, y_cible, couleur_cible_finale

    n=random.randint(1,3)  
    if n==1:  
        x_cible=11
        y_cible=3
    if n==2:
        x_cible=5
        y_cible=13
    if n==3:
        x_cible=1
        y_cible=2
    #x1, y1 = random.randint(0,LARGEUR//COTE - 1), random.randint(0,HAUTEUR//COTE - 1)
    #x2, y2= x1 + 1, y1 +1
    
    couleur_cible_finale = random.choice(couleur_cible)
    carre = canvas.create_rectangle((x_cible*COTE, y_cible*COTE),((x_cible+1)*COTE, (y_cible+1)*COTE),fill=couleur_cible_finale)
    couleur_cible.remove(couleur_cible_finale)
    return carre

n_robot = 0

def clic(event):
    # position du pointeur de la souris
    global X, Y, x0, y0, x1, y1, x2, y2, x3, y3, n_robot
    X = event.x / 30
    Y = event.y / 30
    print(X, Y)

    #touche = event.keysym
    if X >= x0 and X <= x0+1 :
            if Y >= y0 and Y <= y0+1 :
                n_robot = 0
            print("clic: robot1")
    elif X >= x1 and X <= x1+1 :
            if Y >= y1 and Y <= y1+1 :
                n_robot = 1
            print( "clic: robot2")
    elif X >= x2 and X <= x2 + 1 :
            if Y >= y2 and Y <= y2 + 1 :
                n_robot = 2
            print("clic: robot3")
    elif X >= x3 and X <= x3 + 1 :
            if Y >= y3 and Y <= y3 + 1 :
                n_robot = 3
            print( "clic: robot4")



def mon_reset(event):
    touche = event.keysym
    if touche == "space":
        print("space appuyé")
        resetMap()


def deplacement_robot(event): 
    # Sélection du robot à déplacer puis déplacement avec les touches directionnelles du clavier
    global X, Y, x0, y0, x1, y1, x2, y2, x3, y3, n_robot, MurdeGauche, MurduHaut,x_cible,y_cible,couleur_cible_finale
    global score
    X = event.x / 30
    Y = event.y / 30
    print(X, Y)
    print(x0,y0)
    touche = event.keysym
    score=score+1
    print("score = ", score)

    if n_robot == 0 :
                if touche == "Up":# Déplacement du robot vers le haut
                    while MurduHaut[y0][x0] == 0 or y0 == 14 :
                        y0=y0-1
                        if (x0==x1 and y0==y1) or (x0==x2 and y0==y2) or (x0==x3 and y0==y3): 
                            y0=y0+1
                            break 
                        canvas.move(robot1, 0,-30)
                    
                    
                elif touche == "Down": # Déplacement du robot vers le bas
                    if y0!=15:
                        while MurduHaut[y0+1][x0] == 0 or y0 == 14:
                            y0=y0+1
                            if (x0==x1 and y0==y1) or (x0==x2 and y0==y2) or (x0==x3 and y0==y3): 
                                y0=y0-1
                                break 
                            canvas.move(robot1, 0, 30)
                            print("down:",x0,y0)
                            if y0==15:
                                break
                        
                elif touche == "Right": # Déplacement du robot vers la droite
                    if x0!= 15 :
                        while x0 == 14 or  MurdeGauche[y0][x0+1] == 0 :
                            x0=x0+1
                            if (x0==x1 and y0==y1) or (x0==x2 and y0==y2) or (x0==x3 and y0==y3): 
                                x0=x0-1
                                break
                            print(x0,y0)
                            canvas.move(robot1, 30, 0)
                            if x0 == 15:
                                break
                        
                elif touche == "Left": # Déplacement du robot vers la gauche
                    while MurdeGauche[y0][x0] == 0 or x0 == 14:
                        x0=x0-1
                        if (x0==x1 and y0==y1) or (x0==x2 and y0==y2) or (x0==x3 and y0==y3): 
                                x0=x0+1
                                break
                        canvas.move(robot1, -30, 0)
                    
                print(touche, "robot1")
                if x0==x_cible and y0==y_cible and couleur_cible_finale=="red":
                    print("le robot 1 a gagné avec un score de ",score)
    elif n_robot == 1 :
                if touche == "Up":# Déplacement du robot vers le haut
                    while MurduHaut[y1][x1] == 0 or y1 == 14 :
                        y1=y1-1
                        if (x1==x0 and y1==y0) or (x1==x2 and y1==y2) or (x1==x3 and y1==y3): 
                            y1=y1+1
                            break
                        
                        canvas.move(robot2, 0,-30)
                elif touche == "Down": # Déplacement du robot vers le bas
                    if y1!=15:
                        while MurduHaut[y1+1][x1] == 0 or y1 == 14:
                            y1=y1+1
                            if (x1==x0 and y1==y0) or (x1==x2 and y1==y2) or (x1==x3 and y1==y3): 
                                y1=y1-1
                                break
                            canvas.move(robot2, 0, 30)
                            print("down:",x1,y1)
                            if y1==15:
                                break
                elif touche == "Right": # Déplacement du robot vers la droite
                    if x1!= 15 :
                        while x1 == 14 or  MurdeGauche[y1][x1+1] == 0 :
                            x1=x1+1
                            if (x1==x0 and y1==y0) or (x1==x2 and y1==y2) or (x1==x3 and y1==y3): 
                                x1=x1-1
                                break
                            print(x1,y1)
                            canvas.move(robot2, 30, 0)
                            if x1 == 15:
                                break
                elif touche == "Left": # Déplacement du robot vers la gauche
                    while MurdeGauche[y1][x1] == 0 or x1 == 14:
                        x1=x1-1
                        if (x1==x0 and y1==y0) or (x1==x2 and y1==y2) or (x1==x3 and y1==y3): 
                                x1=x1+1
                                break
                        canvas.move(robot2, -30, 0)
                print(touche, "robot2")
                if x1==x_cible and y1==y_cible and couleur_cible_finale=="blue":
                    print("le robot 2 a gagné avec un score de ",score)
    elif n_robot == 2 :
                if touche == "Up":# Déplacement du robot vers le haut
                    while MurduHaut[y2][x2] == 0 or y2 == 14 :
                        y2=y2-1
                        if (x2==x0 and y2==y0) or (x2==x1 and y2==y1) or (x2==x3 and y2==y3): 
                                y2=y2+1
                                break
                        canvas.move(robot3, 0,-30)
                elif touche == "Down": # Déplacement du robot vers le bas
                    if y2!=15:
                        while MurduHaut[y2+1][x2] == 0 or y2 == 14:
                            y2=y2+1
                            if (x2==x0 and y2==y0) or (x2==x1 and y2==y1) or (x2==x3 and y2==y3): 
                                y2=y2-1
                                break
                            canvas.move(robot3, 0, 30)
                            print("down:",x2,y2)
                            if y2==15:
                                break
                elif touche == "Right": # Déplacement du robot vers la droite
                    if x2!= 15 :
                        while x2 == 14 or  MurdeGauche[y2][x2+1] == 0 :
                            x2=x2+1
                            if (x2==x0 and y2==y0) or (x2==x1 and y2==y1) or (x2==x3 and y2==y3): 
                                x2=x2-1
                                break
                            print(x2,y2)
                            canvas.move(robot3, 30, 0)
                            if x2 == 15:
                                break
                elif touche == "Left": # Déplacement du robot vers la gauche
                    while MurdeGauche[y2][x2] == 0 or x2 == 14:
                        x2=x2-1
                        if (x2==x0 and y2==y0) or (x2==x1 and y2==y1) or (x2==x3 and y2==y3): 
                                x2=x2+1
                                break
                        canvas.move(robot3, -30, 0)
                print(touche, "robot3")
                if x2==x_cible and y2==y_cible and couleur_cible_finale=="yellow":
                    print("le robot 3 a gagné avec un score de ",score)
    elif n_robot == 3 :
                if touche == "Up":# Déplacement du robot vers le haut
                    while MurduHaut[y3][x3] == 0 or y3 == 14 :
                        y3=y3-1
                        if (x3==x0 and y3==y0) or (x3==x1 and y3==y1) or (x3==x2 and y3==y2): 
                                y3=y3+1
                                break
                        canvas.move(robot4, 0,-30)
                elif touche == "Down": # Déplacement du robot vers le bas
                    if y3!=15:
                        while MurduHaut[y3+1][x3] == 0 or y3 == 14:
                            y3=y3+1
                            if (x3==x0 and y3==y0) or (x3==x1 and y3==y1) or (x3==x2 and y3==y2): 
                                y3=y3-1
                                break
                            canvas.move(robot4, 0, 30)
                            print("down:",x3,y3)
                            if y3==15:
                                break
                elif touche == "Right": # Déplacement du robot vers la droite
                    if x3!= 15 :
                        while x3 == 14 or  MurdeGauche[y3][x3+1] == 0 :
                            x3=x3+1
                            if (x3==x0 and y3==y0) or (x3==x1 and y3==y1) or (x3==x2 and y3==y2): 
                                x3=x3-1
                                break
                            print(x3,y3)
                            canvas.move(robot4, 30, 0)
                            if x3 == 15:
                                break
                elif touche == "Left": # Déplacement du robot vers la gauche
                    while MurdeGauche[y3][x3] == 0 or x3 == 14:
                        x3=x3-1
                        if (x3==x0 and y3==y0) or (x3==x1 and y3==y1) or (x3==x2 and y3==y2): 
                                x3=x3+1
                                break
                        canvas.move(robot4, -30, 0)
                print(touche, "robot4")
                if x3==x_cible and y3==y_cible and couleur_cible_finale=="green":
                    print("le robot 4 a gagné avec un score de ",score)

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
    global robot1, robot2, robot3, robot4

    x0, y0 = robot1_start_pos_X, robot1_start_pos_Y
    x1, y1 = robot2_start_pos_X, robot2_start_pos_Y
    x2, y2 = robot3_start_pos_X, robot3_start_pos_Y
    x3, y3 = robot4_start_pos_X, robot4_start_pos_Y
    score=0
    
    canvas.moveto(robot1, x0*30, y0*30)
    canvas.moveto(robot2, x1*30, y1*30)
    canvas.moveto(robot3, x2*30, y2*30)
    canvas.moveto(robot4, x3*30, y3*30)

# programme principale
racine = tk.Tk()
racine.title("Robot ricochet")

# création des widgets
canvas = tk.Canvas(racine, width = HAUTEUR, height = LARGEUR, bg = COULEUR_FOND)

# exécution des fonctions

quadrillage()

MurG = 0
MurH = 0

MurdeGauche = ((1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0),(1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0),(1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0),(1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0),(1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),(1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0),(1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0),(1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0),(1,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0),(1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0),(1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0),(1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),(1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0),(1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0),(1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0),(1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0))
MurduHaut = ((1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0),(0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0),(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1),(0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0),(0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0),(1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0),(0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0),(0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0),(0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0),(0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1),(0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0),(1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0),(0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0),(0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0),(0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0))

def terraindejeu(gauche,haut):
    """trace les murs d'un terrain de jeu à partir de matrices"""
    global MurG 
    global MurH

    MurG = gauche
    MurH = haut

    for i in range(len(gauche)):
        for j in range(len(gauche[i])):
            if gauche[i][j] == 1 :
                canvas.create_line((j*COTE,i*COTE),(j*COTE,(i+1)*COTE),fill = "black", width = 10)
    
    for i in range(len(haut)):
        for j in range(len(haut[i])):
            if haut[i][j] == 1 :
                canvas.create_line((j*COTE,i*COTE),((j+1)*COTE,i*COTE),fill = "black", width = 10)


terraindejeu(MurdeGauche,MurduHaut )



#murs extérieurs
canvas.create_line((0,0),(0,HAUTEUR),fill = "black", width = 10)
canvas.create_line((0,0),(LARGEUR,0),fill = "black", width = 10)
canvas.create_line((LARGEUR,0),(LARGEUR,HAUTEUR),fill = "black", width = 10)
canvas.create_line((0,HAUTEUR),(LARGEUR,HAUTEUR),fill = "black", width = 10)

cible = trace_cible()
robot1 = trace_robot1()
robot2 = trace_robot2()
robot3 = trace_robot3()
robot4 = trace_robot4()
robot = [robot1, robot2, robot3, robot4]

#placement des widgets
canvas.grid()

#exécution des évènements
canvas.bind("<Button-1>", clic)
canvas.bind_all("<Up>", deplacement_robot)
canvas.bind_all("<Down>", deplacement_robot)
canvas.bind_all("<Right>", deplacement_robot)
canvas.bind_all("<Left>", deplacement_robot)
canvas.bind_all("<space>", mon_reset)

racine.mainloop()