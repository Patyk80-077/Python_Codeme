# Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową,
# która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.

#your code goes here
Waga = float(input('Podaj wagę [kg]'))
Wzrost = float(input('Podaj wzrost [m]'))
BMI = Wzrost/((Waga)*(Waga))

if BMI < 18.5:
    print('Niedowaga')
elif 18.5 <= BMI < 25:
    print('Waga Prawidłowa')
elif 25 <= BMI < 30:
    print('Nadwaga')
else:
    print('Otyłość')