# robot_ricochet

Bienvenue dans le readme de notre projet qui consiste à créer un plateau de jeu nommé robot ricochet.
Ce jeu est composé de quatre robots respectivement de couleur rouge, jaune, verte et bleue. 
À tous les robots est attribuée une unique cible qu'ils devront atteindre.
Sur le plateau, il y'a de nombreux murs dispersés qui seront des obstacles pour les robots.
Le but du jeu est donc qu'un robot atteigne la cible en réussisant à surmonter les obstacles.

## <h2 id="top">Sommaire</h2>
---
-[Programme](#programme)  
-[Contrôles](#controles)  
-[Bugs et problèmes non résolus](#bugs)  
-[Librairies externes](#libs)

## <h2 id="programme">Programme</h2>
---
Le programme, quand on l'excécute crée un canvas dans lequel se trouvent des murs en forme d'angle droit, des robots respectivement jaune, bleu, rouge et vert, leur cible et enfin un carré central. 

Tout d'abord, nous avons généré un canvas quadrillé avec des dimensions données : 16x16

Pour que les robots apparaissent, nous avons créé une fonction qui choisit aléatoirement des coordonnées pour chaque robot dans le canvas, la fonction pour la cible est assez similaire, en effet la fonction génère aléatoirement des coordonnées pour le carré, autrement dit pour la cible. Dans ces fonctions nous avons du prendre en compte les dimensions du canvas ainsi que les localisations des murs afin que les robots et les cibles soient placés correctement et ne soient pas en dehors du canvs ou confondus avec les murs.

Nous avons aussi crée une fonction qui fait apparaitre des murs à des endoits donnés, ces murs sont des obstacle pour les robots. 

Nous avons de plus élaboré une fonction qui dès lors que l'on clique sur un robot, on le selectionne. Cette fonction a été assosciée à une seconde fonction qui elle, permet de déplacer le robot selectionné grâce aux fleches de notre clavier, ce robot doit se deplacer en ligne droite jusqu'à ce qu'il atteigne un obstacle et ce robot ne doit pas depasser les limites du canvas. 

Une autre fonction permet aussi de compter le nombre de déplacement du robot sélectionné tandis qu'une autre permet de faire retourner le robot à sa position initiale en cliquant sur la touche espace du clavier.

Enfin, une fonction permet d'indiquer que la cible est atteinte et une autre fait disparaitre la cible quand cette dernière est atteinte. 

Ainsi, lorsque l'utilsateur clique sur le bouton pour executer le programme, le canvas quadrillé avec les robots, les murs et la cible apparaissent. Pour jouer au jeu il suffit donc à l'utilisateur de cliquer sur le robot de son choix et de laisser la souris positionnée sur le robot pour pouvoir le deplacer à travers le canvas en essayant de surmonter les obstacles jusqu'à enfin atteindre la cible et voir un message indiquant " la cible est atteinte" apparaître et cette dernière disparaîtra. L'utilisateur peut aussi s'il le souhaite faire revenir le robot à sa position initiale en appuyant sur la touche espace de son clavier.

## <h2 id="controles">Contrôles</h2>
---
-Un clic normal(gauche) de la souris pour selectionner un robot.

-Les flèches du clavier (haut, bas, droite, gauche° pour déplacer les robots.

-La touche espace du clavier pour que le robot utilisé retourne à sa position initiale.

## <h2 id="bugs">Bugs et problèmes non résolus</h2>
---
-Le robot sort du canvas quand on le déplace.

-La fonction "la cible est atteinte" n'a pas été créée.

-Par moment, il se peut que soit la cible soit un des robots se trouvent dans le carré central.

-Les robots se déplacent case par case alors que normalement ils se deplacent en ligne tant qu'il n'y a pas d'obstacle.

-La cible ne disparaît pas quand le robot l'atteint.

## <h2 id="libs">Librairies externes</h2>
---
**Ce projet utilise:**  
-TKinter

-Random

[Haut de la page](#top)
