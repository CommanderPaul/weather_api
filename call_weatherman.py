import requests
import json


class CallWeatherman:

    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?{}{}"
    FUNCTION = "id=5746545"
    API_KEY = "&APPID=7f283940189575de586b368bad666ed1"

    def __init__(self):

        self.temperature = 0

    def execute(self):

        response = requests.get(self.BASE_URL.format(self.FUNCTION, self.API_KEY))
        if response.status_code != 200:
            # This means something went wrong.
            print('GET /tasks/ {}'.format(response.status_code))

        return_bin = b""
        for response_part in response:
            return_bin += response_part

        self.find_temperature(return_bin)

    def find_temperature(self, json_object):

        weather_dict = json.loads(json_object.decode())
        kelvin = (weather_dict['main']['temp'])
        fahrenheit = (kelvin - 273.15) * 9/5 + 32
        fahrenheit_rounded = round(fahrenheit, 2)
        self.temperature = fahrenheit_rounded
        return fahrenheit_rounded


if __name__ == "__main__":

    wet = CallWeatherman()
    wet.execute()
