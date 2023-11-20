#!/usr/bin/python3
"""contains the class definition of a City
and an instance <Base = declarative_base()>
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """<City> class that inherits from Base
    links to the MySQL table <states>
    id(int): column
    name(string): column
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
