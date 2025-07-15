age = int(input("Entrez votre âge : "))
pays = input("Entrez votre pays : ").lower()

if age >= 18 and (pays == "congo" or pays == "cameroun"):
    print("Inscription autorisée.")
elif age < 18 :
    print("vous êtes trop jeune pour vous inscrire.")
else:
    print("Désolé, programme réservé aux ressortissants du congo ou comeroun.")
