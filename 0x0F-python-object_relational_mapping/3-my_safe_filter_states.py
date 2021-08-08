#!/usr/bin/python3

""" lists all states from the database hbtn_0e_0_usa

    connect to the database hbtn_0e_0_usa and list all the records of
    the field id, states order by id

    methods:
    take_argument()
    connect_to_db()
    perform_operations()
"""
from sys import argv
import MySQLdb


def take_arguemnts():
    """Take arguments from cmd
    Returns:
        Dict: The data to connect a database.
    """
    acces_data = {}
    acces_data['user'] = argv[1]
    acces_data['password'] = argv[2]
    acces_data['db_name'] = argv[3]

    return (acces_data)


def connect_to_db():
    """Connects to the database with the specified arguments
    Returns:
        Object: Data base connection
    """
    acces_data = take_arguemnts()
    db = MySQLdb.connect('localhost', acces_data['user'],
                         acces_data['password'], acces_data['db_name'])

    return db


def perform_operations():
    """performs the specified operations on the data base"""

    db = connect_to_db()
    cursor = db.cursor()
    user_input = argv[4]

    sql = """SELECT
                id, name
            FROM
                states
            WHERE
                '%s' LIKE BINARY name
            ORDER BY id ASC""" % user_input

    cursor.execute(sql)
    results = cursor.fetchall()
    for i in results:
        print(i)

    db.close()


if __name__ == "__main__":
    import sys
    import MySQLdb
    take_arguemnts()
    connect_to_db()
    perform_operations()
