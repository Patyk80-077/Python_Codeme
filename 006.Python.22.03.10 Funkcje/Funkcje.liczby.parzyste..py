# Napisać funkcję, która sprawdza czy liczba jest parzysta.

def jest_parzysta():
    n = input('podaj liczbe 1-100: ')
    if str(n) % 2 == 0:
        n = 'jest parzysta'
    else:
        n = 'jest nieparzysta'

    return n

print ("liczba jest_parzysta:(n)")


