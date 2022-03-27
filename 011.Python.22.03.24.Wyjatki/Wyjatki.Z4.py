# Oblicz średnią arymetyczną z kilku liczb.
# Liczby będą podane przez użytkownika po przecinku.
# Napisz funkcję, która przyjmie wartości i wyświetli średnią.
# Program powinen być odporny na błędy użytkownika.
# Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku.

numbers = [12.3, 1.5, 3, 8, 15, 123.345]

def avg(x):

    suma = 0
    for i in x:
        suma = suma + i
        return suma /len(x)
    print("Średnia arytmetyczna wynosi: " + str(avg(numbers)))

    while (IndexError):
    print('To niest to czego oczekujemy')

# program nie działa!!!


