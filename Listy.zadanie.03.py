# Dla podanej przez użytkownika liście liczb całkowitych
# sprawdź czy pierwszy i ostatni element są takie same.

items = ['namiot', 'latarka', 'bidon', 'namiot']

counter = len(items) # Funkcja len() informuje nas z jak wielu znaków składa się napis. Zliczane są również spacje i znaki przestankowe.
first = items[0]
last = items[counter-1]

print(first == last)

print(items[0] == items[-1])