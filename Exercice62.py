choix = None

while choix != "0":
    print("\nMenu :")
    print("1 → Dire bonjour")
    print("2 → Additionner deux nombres")
    print("0 → Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        print("Bonjour !")
    elif choix == "2":
        a = float(input("Nombre 1 : "))
        b = float(input("Nombre 2 : "))
        print(f"Résultat : {a + b}")
    elif choix != "0":
        print("Choix invalide.")
