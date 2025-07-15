liste = list(map(int, input("Entrez des nombres séparés par des espaces : ").split()))

n = len(liste)
for i in range(n):
    for j in range(0, n - i - 1):
        if liste[j] > liste[j + 1]:
            liste[j], liste[j + 1] = liste[j + 1], liste[j]

print("Liste triée :", liste)
