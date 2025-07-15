chaine = input("Entrez une chaîne : ")
inverse = ""

for caractere in chaine:
    inverse = caractere + inverse

print(f"Chaîne inversée : {inverse}")
