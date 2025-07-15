entrée = input("Entrez une liste de nombres : ")
liste = entrée.split()
elements_pairs = liste[::2]
print(f"Éléments aux indices pairs : {elements_pairs}" )
