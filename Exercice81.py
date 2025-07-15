livres = [
    {"titre": "Livre A", "auteur": "Auteur A", "année": 2005},
    {"titre": "Livre B", "auteur": "Auteur B", "année": 2015},
    {"titre": "Livre C", "auteur": "Auteur C", "année": 2022},
]

print("Livres publiés après 2010 :")
for livre in livres:
    if livre["année"] > 2010:
        print(f"{livre['titre']} ({livre['année']})")
