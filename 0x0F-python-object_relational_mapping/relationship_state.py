#!/usr/bin/python3
"""contains the class definition of a State
and an instance <Base = declarative_base()>
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """<State> class that inherits from Base
    links to the MySQL table <states>
    id(int): column
    name(string): column
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade='all, delete-orphan')
