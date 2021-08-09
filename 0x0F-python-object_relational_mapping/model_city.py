#!/usr/bin/python3
"""Contains the class definition of a City
    class:
        City
    """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """Declarative class that defines the columns and
        maps the cities table in the mysql database.

    Args:
        Base : Super class describing the directives to the database
        table that will be mapped.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(256), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
