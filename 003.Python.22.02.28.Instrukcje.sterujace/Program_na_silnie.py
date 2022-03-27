# Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N
# (N podane przez użytkownika, ale nie większe niż 8).
# Przykłady:
# 0! = 1
# 1! = 1
# 3! = 1⋅2⋅3 = 6
# 4! = 1⋅2⋅3⋅4 = 24
# 6! = 1⋅2⋅3⋅4⋅5⋅6 = 720

# n = 0 silnia(n) = 1
# n > 0 silnia(n) = n * silnia(n-1)

def silnia(i): # Definicja funkcji silnia.
    if i == 0:
        return 1
    else:
        return i * silnia(i-1)

def main(): # Definicja funkcji o nazwie main().
    print("Program oblicza 8!, wykorzystując mechanizm rekurencji.")

    print()

    for i in range(0, 9):
        print(i, "!=", silnia(i), ".", sep = "") #wyświetlenie obliczonej silni.
    main() # wywołanie funkcji main().
