"""This module managements the persistence"""

import sqlite3
from sqlite3 import Error


class DataBase(object):
    """This class managements """

    @staticmethod
    def sql_connection():
        """Create a connection to database and make a cursor"""
        try:
            connection = sqlite3.connect('glossary.db')
            cursor = connection.cursor()
            return connection, cursor
        except Error:
            print(Error)

    @staticmethod
    def sql_close():
        """Close cursor and connection to database"""
        connection, cursor = DataBase.sql_connection()
        cursor.close()
        connection.close()
        print("Cursor and connection closed")

    @staticmethod
    def sql_select(get_queries):
        set_queries = get_queries
        connection, cursor = DataBase.sql_connection()
        cursor.execute(set_queries)
        for register in cursor:
            return register


db = DataBase()
