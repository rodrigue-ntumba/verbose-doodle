plat = input("Choisissez un type de plat (viande, poisson, végétarien) : ").lower()

if plat == "viande":
    cuisson = input("Cuisson (saignant, à point, bien cuit) : ")
    print(f"Vous avez choisi une viande {cuisson}.")
elif plat == "poisson":
    sauce = input("Sauce (citron, beurre) : ")
    print(f"Vous avez choisi un poisson avec une sauce {sauce}.")
elif plat == "végétarien":
    option = input("Souhaitez-vous une salade ou des pâtes ? : ")
    print(f"Vous avez choisi un plat végétarien avec {option}.")
else:
    print("Choix non reconnu.")
