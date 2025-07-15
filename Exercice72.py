liste = input("Entrez une liste de valeurs : ").split()
uniques = []

for val in liste:
    if val not in uniques:
        uniques.append(val)

print("Valeurs uniques :", uniques)
