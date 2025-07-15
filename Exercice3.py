heures = int(input("Heures : "))
minutes = int(input("Minutes : "))
secondes = int(input("Secondes : "))

total_secondes = heures * 3600 + minutes * 60 + secondes
print(f"Durée totale en secondes : {total_secondes}")
