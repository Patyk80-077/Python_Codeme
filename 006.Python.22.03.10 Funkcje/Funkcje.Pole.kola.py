# Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia.

import math
def obwód_koła(r):
    pi = 3.14
    print('Pole koła wynosi: ', 2 * pi * (r**2))
radius = float(input('Podaj promień r -> '))
obwód_koła(radius)

