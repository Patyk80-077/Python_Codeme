# Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.

Lista = [1,2,3,4,5,6,7,8,9,10]
Nieparzyste = [i for i in Lista if i %  2!=0 ]
print(Nieparzyste)
