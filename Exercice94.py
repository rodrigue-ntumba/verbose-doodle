phrase = input("Entrez un titre ou une phrase : ")
mots = phras.split()
acronyme = ""

for mot in mots :
    acronyme+=mot[0].upper()
print(f"Acronyme : {acronymme}")
