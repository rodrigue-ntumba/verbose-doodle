nom = input("Nom du produit : ")
prix = float(input("Prix : "))
stock = int(input("Stock : "))
remise = float(input("Remise (%) : "))

prix_final = prix * (1 - remise / 100)

print("\n--- Fiche Produit ---")
print(f"Nom : {nom}")
print(f"Prix initial : {prix} €")
print(f"Remise : {remise} %")
print(f"Prix après remise : {prix_final:.2f} €")
print(f"Stock : {stock} unités")
