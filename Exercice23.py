montant_ht = float(input("Montant HT : "))
taux_tva = float(input("Taux de TVA (%) : "))

montant_ttc = montant_ht * (1 + taux_tva / 100)
print(f"Montant TTC : {montant_ttc:.2f} €")
