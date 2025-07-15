nombres = list(map(float, input("Entrez une liste de nombres : ").split()))

maximum = max(nombres)
minimum = min(nombres)
moyenne = sum(nombres) / len(nombres)

print(f"Maximum : {maximum}")
print(f"Minimum : {minimum}")
print(f"Moyenne : {moyenne:.2f}")
