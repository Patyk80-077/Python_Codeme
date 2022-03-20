# Utwórz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10,
# wypełnioną wynikami mnożenia wiersz × kolumna.

N = 10
print("Program wyświetla tabliczkę mnożenia dla liczb od 1 do 100.")
print()

for wiersze in range(N):
    for kolumny in range(N):
        print((wiersze +1) * (kolumny +1), "\t", end = "")
    print()
