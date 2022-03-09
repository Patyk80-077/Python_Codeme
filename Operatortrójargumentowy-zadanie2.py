# Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
# Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.

liczba1 = int(input("Podaj pierwszą liczbę całkowitą w skali 1-100: "))
liczba2 = int(input("Podaj drugą liczbę całkowitą w skali 1-100" ))


if liczba1 + liczba2 > 100:
    print('liczba1 + liczba2 wynik', liczba1 + liczba2)
else:
    print('Koniec')