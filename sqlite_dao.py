#!/usr/bin/env python3
"""
Program to write to sqlite3.
Created 3/2019
"""

import sqlite3


class SqLiteDao:

    def __init__(self):
        print("beans")
        pass

    def execute(self):

        conn = sqlite3.connect('test.db')


        print("finished!")




if __name__ == "__main__":

    lite_data = SqLiteDao()
    lite_data.execute()
