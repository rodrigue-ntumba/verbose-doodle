phrase = input("Entrez une phrase : ")
mot = input("Mot à masquer : ")

masque = "*" * len(mot)
nouvelle_phrase= phrase.replace(mot,masque)
print(f"Phrase après masquage :{nouvelle_phrase}")
