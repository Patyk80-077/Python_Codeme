# Stwórz listę 10 elementową (różne typy!). Pozwól użytkownikowi podać dowolny index.
# Podziel 1 przez liczbę pod indexem wybranym przez użytkownika. Obsłuż błędy.

list = [1, 2.4, 'Ela', [10], range(9), {32}, 00, 1/3, 1 == 2, 12]

try:

    element = int(input('Podaj dowolny indeks z listy: '))
    list_element = list[element]
    print(list_element)
    1/ list_element
except (TypeError, IndexError) as e:
    print('Poza wyborem')
except ValueError:
    print('Ey, To nie jest dobra wartość')

