nombre = int(input("Entrez un nombre : "))

print(f"\nTable de multiplication de {nombre} :")
for i in range(1, 13):
    print(f"{nombre} x {i} = {nombre * i}")
