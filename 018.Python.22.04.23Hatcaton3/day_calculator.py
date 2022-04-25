from datetime import datetime

def diff_dates():
    choosen_date = input('Podaj wybraną przez siebie datę (max. 7 dni do przodu) w formacie DD-MM-YYYY.\n')
    diff_dates = number_of_days(choosen_date)
    print(diff_dates)
    return diff_dates


def number_of_days(choosen_date):
    date_format = "%d-%m-%Y"
    now = datetime.now()

    future_date = datetime.strptime(choosen_date, date_format)
    diff_dates = future_date - now
    diff_dates = int(diff_dates.days)+1
    return (diff_dates)


# if __name__ == '__main__':
#     main()