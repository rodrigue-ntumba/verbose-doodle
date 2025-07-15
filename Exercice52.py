nombres = input("Entrez des entiers séparés par des espaces : ")
liste = list(map(int, nombres.split()))

somme_pairs = sum(n for n in liste if n % 2 == 0)

print(f"Somme des éléments pairs : {somme_pairs}")

