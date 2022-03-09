# Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
# Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.

x = int(input("Podaj pierwszą dowolną liczbę 1-100: "))
y = int(input("Podaj drugą dowolną liczbę 1-100: "))
z = int(input("Podaj trzecią dowolną liczbę 1-100; "))

if (x > y) and (x > z):
    print('maximum = x')
elif (y > x) and (y > z):
    print('maximum = y')
else:
    print('maximum = z')

