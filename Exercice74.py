etudiants = [("Alice", 17), ("Bob", 12), ("Claire", 15), ("David", 9)]

print("Étudiants ayant une note ≥ 15 :")
for nom, note in etudiants:
    if note >= 15:
        print(f"{nom} : {note}")
