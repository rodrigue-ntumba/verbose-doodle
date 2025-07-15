numero = input("Entrez un numéro de téléphone : ")
if len(numero)>3:
    masqué = "*" * (len(numero) - 3) + numero[-3:]
    print(f"Numéro masqué :{masqué}" )
else:
    print("Numéro trop court pour masquer ")
