import sqlite3


class SqLiteDao:

    CREATE_TEMPERATURE_LOG_TABLE = "CREATE TABLE TemperatureLog (timestamp real PRIMARY KEY, temperature real)"
    SELECT_MOST_RECENT_TEMPERATURE = "SELECT MAX(timestamp), temperature FROM TemperatureLog"
    INSERT_INTO_TEMPERATURE = "INSERT INTO TemperatureLog VALUES (?,?)"
    FIVE_MINUTES_IN_SECONDS = 300

    def __init__(self):
        self.conn = sqlite3.connect('weather.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def check_for_expiry(self, timestamp):

        # return either time and temp, or empty - accommodates empty database
        time_and_temp = self.get_temperature()
        most_recent_time_record = time_and_temp[0]

        return_set = ()
        if most_recent_time_record and (timestamp < (most_recent_time_record + self.FIVE_MINUTES_IN_SECONDS)):
            return_set = time_and_temp

        return return_set

    def create_table(self):
        try:
            self.cursor.execute(self.CREATE_TEMPERATURE_LOG_TABLE)
            print("Table created")
        except sqlite3.OperationalError:
            pass

    def get_temperature(self):
        return_object = ""
        try:
            self.cursor.execute(self.SELECT_MOST_RECENT_TEMPERATURE)
            return_object = self.cursor.fetchone()
        except sqlite3.OperationalError:
            print("Error finding most recent temperature")
        return return_object

    def insert_temperature(self, timestamp, temperature):
        success = True
        try:
            input_params = (timestamp, temperature)
            self.cursor.execute(self.INSERT_INTO_TEMPERATURE, input_params)
            self.conn.commit()
        except sqlite3.IntegrityError:
            print("Error inserting time and temperature")
            success = False
        return success

    def close_connection(self):
        self.conn.close()


if __name__ == "__main__":
    pass
