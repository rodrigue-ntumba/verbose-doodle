mot_de_passe = input("Entrez un mot de passe : ")

est_valide = len(mot_de_passe) >= 8 and any(c.isdigit() for c in mot_de_passe) and any(c.isupper() for c in mot_de_passe)

if est_valide:
    print("Mot de passe valide.")
else:
    print("Mot de passe invalide.")
