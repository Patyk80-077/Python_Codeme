# Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce.
# Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty.
# Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

opinia1 = int(input("Podaj pierwszą ocenę w skali 1-10: "))
opinia2 = int(input("Podaj drugą ocenę w skali 1-10: "))
opinia3 = int(input("podaj trzecią ocenę w skali 1-10: "))

if (opinia1 * opinia2 * opinia3) / 3 > 7:
    print("Bardzo dobra!")
elif (opinia1 * opinia2 * opinia3) / 3 >= 5:
    print("Przeciętna")
else:
    print("Nie warta uwagi!!")