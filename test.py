fic = open("test.txt","w")
fic.write("la variable vaut" + str(3.14) + "\n")
fic.write("yay")
fic.close()

import random

fic = open("test.txt", "w")
for i in range(32):
    for i in range(4):
        n = random.randint(0,1)
        fic.write(str(n)+ "\n")
fic.close()

fic = open("test.txt","r")
for ligne in fic :
    print(ligne)
fic.close()

fic = open("test.txt","r")
res = 0
for ligne in fic :
    note = ligne.split()[0]
    res = res + int(note)
fic.close()
print("La somme des notes vaut", res)

var = "Lundi il fait beau"
liste = var.split()
print(liste)

fic = open()