# Stwórz zmienną password. Hasło powinno składać z liter i cyfr,
# zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków.
# Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne.
# Wyświetl różne komunikaty w zależności od rodzaju błędu.

pasword = input("Podaj hasło: ")
if len(pasword) < 8:
    print('Hasło musi mieć minimum 8 znaków')
if pasword.isalpha() or pasword.isdigit():
    print('Hasło musi zawierać zarówno cyfry i litery')
if pasword.islower():
    print('hasło musi zawierać conajmniej jedną dużą literę')
if pasword.isupper():
    print(' hasło musi zawierać conajmniej jedną mała literę')
