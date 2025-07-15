import random

secret = random.randint(1, 100)
essai = None

while essai != secret:
    essai = int(input("Devine le nombre (entre 1 et 100) : "))
    if essai < secret:
        print("Trop petit.")
    elif essai > secret:
        print("Trop grand.")
    else:
        print("Bravo !")
