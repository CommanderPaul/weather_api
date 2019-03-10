#!/usr/bin/env python3
"""
Program to make calls to weather api.
Created 3/2019
"""

import requests
import json


class CallWeatherman:

    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?{}{}"
    FUNCTION = "id=5746545"
    API_KEY = "&APPID="


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




        #print(json_object.decode())





    # def process_filename_args(self):
    #
    #     for target in self.args.file:
    #         with open(target.name) as file_pointer:
    #
    #             while 1:
    #                 character = file_pointer.read(self.READ_SIZE)
    #                 self.process_character(character)
    #                 if not character:
    #                     break  # end of file


if __name__ == "__main__":

    wet = CallWeatherman()
    wet.execute()
