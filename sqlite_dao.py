#!/usr/bin/env python3
"""
Program to write to sqlite3.
Created 3/2019
"""

import sqlite3


class SqLiteDao:

    def __init__(self):
        self.conn = sqlite3.connect('weather.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):

        try:
            self.cursor.execute(
                '''
                CREATE TABLE TemperatureLog
                 (timestamp real PRIMARY KEY, temperature real)
                '''
            )
        except sqlite3.OperationalError:
            pass

    def get_temperature(self):
        return_object = ""
        try:
            self.cursor.execute(
                '''
                SELECT MAX(timestamp), temperature FROM TemperatureLog 
                '''
            )

            return_object = self.cursor.fetchone()

        except sqlite3.OperationalError:
            print("aww")


        return return_object


    def insert_temperature(self, timestamp, temperature):
        try:
            # params need to be a tuple, or a list of tuples
            input_params = (timestamp, temperature)

            self.cursor.execute(
                '''

                INSERT INTO TemperatureLog VALUES (?,?)

                ''', input_params

            )
            self.conn.commit()
        except sqlite3.IntegrityError:
            print("oops2")

    def close_connection(self):
        self.conn.close()


if __name__ == "__main__":

    lite_data = SqLiteDao()
    lite_data.execute()
