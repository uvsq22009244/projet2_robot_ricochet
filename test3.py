
fic = open("notes.txt", "r")
for ligne in fic:
    print(ligne)
fic.close()


res = 0
fic = open("notes.txt", "r")

for ligne in fic:
    note = ligne.split()[0]
    res = res + int(note)
fic.close()
print("La somme des notes vaut", res)


for i in range(len(G)):
    for j in range(len(G[i])):
        if G[i][j] == 1 :
            canvas.create_line((j*COTE,i*COTE),(j*COTE,(i+1)*COTE),fill = "blue", width = 20)

for i in range(len(H)):
    for j in range(len(H[i])):
        if H[i][j] == 1 :
            canvas.create_line((j*COTE,i*COTE),((j+1)*COTE,i*COTE),fill = "blue", width = 20)

