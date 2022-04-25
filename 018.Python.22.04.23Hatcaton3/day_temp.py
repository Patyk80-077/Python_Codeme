import requests
import json
from datetime import datetime


def main(number_of_days):

    key = "d7d33bcda62df8c3afe884bbb7c390a7"
    gdansk = (54.372158, 18.638306)

    url = f'https://api.openweathermap.org/data/2.5/onecall?lat=' \
          f'{gdansk[0]}&lon={gdansk[1]}&exclude=current,minutely,hourly,alerts&appid={key}&units=metric'

    response = requests.get(url)
    data = json.loads(response.text)
    days = []
    day_temp = {
        "date": "",
        "sunrise": "",
        "sunset": "",
        "tmin": 0,
        "tmax": 0,
        "tday": 0,
        "tnight": 0,
        "pressure": 0,
        "humidity": 0,
        "wind_speed": 0,
        "weather": "",
        "cloudiness": 0
    }
    counting_days = -1
    for day in data["daily"]:
        if counting_days < number_of_days:
            day_temp["date"] = datetime.utcfromtimestamp(day["dt"]).strftime('%Y-%m-%d')
            day_temp["sunrise"] = datetime.utcfromtimestamp(day["sunrise"]).strftime('%H:%M:%S')
            day_temp["sunset"] = datetime.utcfromtimestamp(day["sunset"]).strftime('%H:%M:%S')
            day_temp["tmin"] = day["temp"]["min"]
            day_temp["tmax"] = day["temp"]["max"]
            day_temp["tday"] = day["temp"]["day"]
            day_temp["tnight"] = day["temp"]["night"]
            day_temp["pressure"] = day["pressure"]
            day_temp["humidity"] = day["humidity"]
            day_temp["wind_speed"] = day["wind_speed"]
            day_temp["weather"] = day["weather"][0]['main']
            day_temp["cloudiness"] = day["clouds"]
            days.append(day_temp.copy())
            counting_days = counting_days +1
        else:
            break

    return days