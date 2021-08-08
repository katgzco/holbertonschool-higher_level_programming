#!/usr/bin/python3
""" lists all State objects from the database
    methods:
    take_arguemnts()
    connect_to_db()
    performace_operation()
    """

from sys import argv

from MySQLdb import connect
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def take_arguemnts():
    """Take arguments from cmd
    Returns:
        Dict: The data to connect a database.
    """
    acces_data = {}
    acces_data['user'] = argv[1]
    acces_data['password'] = argv[2]
    acces_data['db_name'] = argv[3]

    return acces_data


def connect_to_db():
    """Accesses the mysql database using the login data provided by the user.

    Returns:
        Engine: Entry point for connection to the database.
    """
    acces_data = take_arguemnts()
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            acces_data['user'], acces_data['password'],
            acces_data['db_name']), pool_pre_ping=True)
    return engine


def performace_operation():
    """performs the transactions in the database by means of the mapped class
    """
    engine = connect_to_db()
    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).first()
    if (instance is not None):
        print('{}: {}'.format(instance.id, instance.name))
    else:
        print('Nothing')


if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    take_arguemnts()
    connect_to_db()
    performace_operation()
