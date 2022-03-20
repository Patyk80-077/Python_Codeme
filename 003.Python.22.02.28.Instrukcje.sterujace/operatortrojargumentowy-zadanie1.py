# Poproś użytkownika o podanie liczby.
# Sprawdź czy liczba podana przez użytkownika jest podzielna przez 3 bez reszty
# i wyświetl komunikat “Twoja liczba jest podzielna przez 3”.

number = input("Podaj liczbę 1-100: ")
number = int (number)
if number % 3 == 0:
    print(f'Liczba {number} jest podzielna przez 3 bez reszty')
else:
    print('Liczba nie jest podzielna przez 3 bez reszty')