# W kodzie BMI ufamy, że użytkownik podaje wartość w kilogramach lub w metrach i rzutujemy do float.
# Co jeśli użytkownik poda wartość 60 kg ?
# Zmodyfikuj kod z ostatnich zajęć tak, aby wykluczyć powyższy przypadek.

import BMI

def show_advice(state):
    filename = state + 'txt'
    with open(filename) as fopen:
        content = fopen.read()

    print('----Twoja porada: ')
    print(content)

def get_user_data():
    try:
        weight = float(input('Podaj swoją wagę [kg]: '))
        height = float(input('Podaj swój wzrost [m] '))
    except:
        print('Wartość niepawidłowa, spróbój jeszcze raz')
    return weight, height

def main():
    w, h = get_user_data()
    result = BMI.get_BMI_value(w,h)
    show_advice(result)



