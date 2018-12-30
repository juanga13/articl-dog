import sqlite3


class PermDataController:
    """

    """

    def __init__(self):
        self.conn = sqlite3.connect("persistent-data.db")

        self.c = self.conn.cursor()

        self.c.execute("""CREATE TABLE IF NOT EXISTS favouritearticles (
                          id integer primary key AUTOINCREMENT,
                          title text,
                          summary text,
                          text text,
                          images text,
                          publish_date text)""")

        self.c.execute("""CREATE TABLE IF NOT EXISTS settings (
                          name text,
                          value integer)""")
        self.conn.commit()

    def add_data(self, article_data):
        self.c.execute("""INSERT INTO favouritearticles 
                          VALUES (?, ?, ?, ?, ?)""",
                       article_data)

    def setup_settings(self, settings):
        self.c.executemany("""INSERT INTO favouritearticles 
                              VALUES (?, ?)""",
                           settings)

    def edit_setting(self, setting_name, new_value):
        self.c.execute("""""")

    def close_conn(self):
        self.conn.close()
