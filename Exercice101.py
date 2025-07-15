mot = input("Entrez un mot d'au moins 5 lettres : ")

if len(mot) >= 5:
    milieu = mot[2:-2]
    print("Partie centrale :", milieu)
else:
    print("Le mot est trop court.")
