#!/usr/bin/env python3
"""
Program to make calls to weather api.
Created 3/2019
"""

import requests


class CallWeatherman:

    base_url = "http://api.openweathermap.org/data/2.5/weather?{}"

    def __init__(self):
        print("beans")
        pass

    def execute(self):

        resp = requests.get(self.base_url.format('id=5746545&APPID=<my api key>'))
        if resp.status_code != 200:
            # This means something went wrong.
            print('GET /tasks/ {}'.format(resp.status_code))
        for todo_item in resp:
            #print('{} {}'.format(todo_item['id'], todo_item['summary']))
            print(todo_item)



        print("finished!")

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
