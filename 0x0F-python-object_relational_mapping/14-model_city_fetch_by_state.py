#!/usr/bin/python3
""" prints all City objects from the database
    methods:
    take_arguemnts()
    connect_to_db()
    performace_operation()
    """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv


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

    Base.metadata.create_all(engine)
    return engine


def performace_operation():
    """performs the transactions in the database by means of the mapped class
    """
    engine = connect_to_db()
    Session = sessionmaker(bind=engine)
    session = Session()

    instances = session.query(State, City).filter(State.id == City.state_id)

    for instance in instances:
        print('{}: ({}) {}'.format(instance.State.name,
              instance.City.id, instance.City.name))


if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City
    from sys import argv
    take_arguemnts()
    connect_to_db()
    performace_operation()
