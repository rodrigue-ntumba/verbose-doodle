prenom = input("Entrez votre prénom : ")
age = int(input("Entrez votre âge : "))
ville = input("Entrez votre ville : ")
metier = input("Entrez votre métier : ")

print("\n=== Profil ===")
print(f"Nom : {prenom}")
print(f"Âge : {age} ans")
print(f"Ville : {ville}")
print(f"Métier : {metier}")

jours_vécus = age * 365  # approximation
print(f"Vous avez vécu environ {jours_vécus} jours.")
