note1 = float(input("Note 1 : "))
note2 = float(input("Note 2 : "))
note3 = float(input("Note 3 : "))

moyenne = (note1 + note2 + note3) / 3

print(f"Moyenne : {moyenne:.2f}")
if moyenne >= 10:
    print("L'étudiant est reçu.")
else:
    print("L'étudiant n'est pas reçu.")
