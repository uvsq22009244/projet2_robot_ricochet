# robot_ricochet

Bienvenue dans le readme de notre projet qui consiste à créer un plateau de jeu nommé robot ricochet.
Ce jeu est composé de quatre robots respectivement de couleur rouge, jaune, verte et bleue. 
À tous les robots est attribuée une unique cible qu'ils devront atteindre.
Sur le plateau il y'a de nombreux murs dispersés qui seront des obstacles pour les robots.
Le but du jeu est donc qu'un robot atteigne sa cible désignée en réussisant à surmonter les obstacles.

## <h2 id="top">Sommaire</h2>
---
-[Implémentations](#implements)  
-[Contrôles](#controles)  
-[Bugs](#bugs)  
-[Librairies externes](#libs)

## <h2 id="implements">Implémentations</h2>
---
Le programme quand on l'excécute crée un canvas dans lequel se trouvents des murs en forme d'angle droit, des robots respectivement jaune, bleu, rouge et vert, leur cible et enfin un carré central. 

Tout d'abord nous avons généré un canvas quadrillé avec des dimensions données : 16x16

Pour que les robots apparaissent nous avons créé une fonction qui choisit aléatoirement des coordonnées pour chaque robot dans le canvas, la fonction pour la cible est assez similaire, en effet la fonction génère aléatoirement des coordonnées pour le carré, autrement dit pour la cible. Dans ces fonctions nous avons du prendre en compte les dimensions du canvas ainsi que les localisations des murs afin que les robots et les cibles soient placés correctement et ne soient pas en dehors du canvs ou confondus avec les murs.

Nous avons aussi crée une fonction qui fait apparaitre des murs à des endoits donnés, ces murs sont des obstacle pour les robots. 

Nous avons élaboré une fonction qui dès lors que l'on clique sur un robot, on le selectionne. Cette fonction a été assosciée à une seconde fonction qui elle, permet de déplacer le robot selectionné grâce aux fleches de notre clavier. 

Une autre fonction permet aussi de compter le nombre de déplacement du robot sélectionné.

Enfin, une fonction permet d'indiquer que la cible est atteinte et une autre fait disparaitre la cible quand cette dernière est atteinte. 

Ainsi, lorsque l'utilsateur clique sur le bouton pour executer le programme, le canvas quadrillé avec les robots, les murs et la cible apparaissent, pour jouer au jeu il suffit donc à l'utilisateur de cliquer sur le robot de son choix et de le deplacer à travers le canvas en essayant de surmonter les obstacles jusqu'à enfin atteindre la cible et voir un message indiquant " la cible est atteinte" apparaître et cette dernière disparaîtra.

## <h2 id="controles">Contrôles</h2>
---


## <h2 id="bugs">Bugs</h2>
---
tu ecris ce que tu veux

## <h2 id="libs">Librairies externes</h2>
---
**Ce projet utilise:**  
-TKinter

[Haut de la page](#top)
