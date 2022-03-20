# Stwórz krotkę liczb całkowitych.
# Poproś użytkownika o podanie dowolnej liczby. Jeśli liczba znajduje się na krotce wyswietl jej indeks.

import random
Numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Number1 = (1, 7)
my_Numbers = random.choice(Number1)
while 1==1:
    y = input("Zgadnij liczbę całkowitą od 1 do 9")

    if int(y) == my_Numbers:
        print("To jest ta liczba!!")
        break
    if int(y) < my_Numbers: print('Podałeś za mała liczbę')
    if int(y) > my_Numbers: print('Podałes za duż liczbę')





