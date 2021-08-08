#!/usr/bin/python3
"""contains the class definition of a State and an
instance Base = declarative_base()
Class:
State
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Declarative class that defines the columns and
        maps the states table in the mysql database.
    Args:
        Base: Super class describing the directives to the database
        table that will be mapped.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
