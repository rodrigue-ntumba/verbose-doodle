panier = float(input("Valeur du panier (€) : "))

if panier >= 100:
    livraison = 0
elif panier >= 50:
    livraison = 5
else:
    livraison = 10

total = panier + livraison

print(f"Frais de livraison : {livraison} €")
print(f"Total à payer : {total:.2f} €")
