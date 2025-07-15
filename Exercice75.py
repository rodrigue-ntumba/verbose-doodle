liste = input("Entrez une liste de valeurs : ").split()
inversée = []

for i in range(len(liste) - 1, -1, -1):
    inversée.append(liste[i])

print("Liste inversée :", inversée)
