# Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.

def show_men():
    print('Wybierz liczbę:  ')
    print('- Wypisz liczbę, by dodać do krotki')
    print(' - Wpisz "koniec", żeby zakończyć program')

numbers = []
while(True):
    show_men()
    choice = input()
    if choice == 'koniec':
        break
    elif choice.isdigit():
        num = int(choice)
        numbers.append(num)
        print('----> dodano')
    else:
        print('Zły wybór. Spróbuj jeszcze raz')

print(numbers)
numbers = tuple(numbers)
print(numbers)



