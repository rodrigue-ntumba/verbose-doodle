temperature = float(input("Température en °C : "))

if temperature >= 35:
    print("Très chaud, restez hydraté.")
elif 25 <= temperature <= 34:
    print("Chaud, faites attention au soleil.")
elif 15 <= temperature <= 24:
    print("Température agréable.")
else:
    print("Il fait frais, couvrez-vous.")
