# Program, będący implementacją gry "wisielec".
#  • Użytkownik ma za zadanie odgadnąć hasło, które ukryte jest w programie.
#  • Program pokazuje ile liter ma hasło i te litery, które zostały już odgadnięte
#  • Użytkownik podaje po jednej literze. Użytkownik ma ograniczoną ilość prób.
#  • W każdym momencie, zamiast podania litery użytkownik może spróbować odgadnąć całe hasło.
#  • Popraw kod wisielca, tak by pobierać hasła do gry z pliku hangman.json.
#    Plik powinnien zawierać conamniej jedno zagnieżdżenie odpowiadające kategoriom, które użytkownik może wybrać w grze.
#    Kategorie pobrane z pliku JSON pojawiają się jako elementy menu start.
# import modułów
import random

# stałe
HANGMAN = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   -+-
     | 
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-
     |   
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |   
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |    |
     |   | 
     |   | 
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |    |
     |   | |
     |   | |
     |  
    ----------
    """)

MAX_WRONG = len(HANGMAN) - 1
WORDS = ["SZWECJA", "ANGLIA", "ESTONIA", "CZECHY", "CHORWACJA"]

# inicjalizacja zmiennych
word = random.choice(WORDS)  # słowo do odgadnięcia
so_far = "-" * len(word)  # kreska zastępuje nieodgadniętą literę
wrong = 0  # liczba nietrafionych liter
used = []  # litery już użyte w zgadywaniu
print(word)
print("Witaj w grze 'Wisielec'.  Powodzenia!")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nWykorzystałeś już następujące litery:\n", used)
    print("\nNa razie zagadkowe słowo wygląda tak:\n", so_far)

    guess = input("\n\nWprowadź literę lub pełne hasło: ")
    guess = guess.upper()
    guess_l = len(guess)
    print(guess_l)

    if (len(str(guess)) <= 1):            # sprawdza, czy ktoś zgaduję jedną literę czy cały wyraz

        while guess in used:
            print("Już wykorzystałeś literę", guess)
            guess = input("Wprowadź literę: ")
            guess = guess.upper()

        used.append(guess)

        if guess in word:
            print("\nTak!", guess, "znajduje się w zagadkowym słowie!")

            # utwórz nową wersję zmiennej so_far, aby zawierała odgadniętą literę
            new = ""
            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                    new += so_far[i]
            so_far = new

        else:
            print("\nNiestety,", guess, "nie występuje w zagadkowym słowie.")
            wrong += 1
    else:
        if guess != word:
            print("\nNiestety,", guess, "nie występuje w zagadkowym słowie.")
            wrong += 1
        else:
            print("")
            break

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nZostałeś powieszony!")
else:
    print("\nOdgadłeś!")


print("\nZagadkowe słowo to", word)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

