#!/usr/bin/python3
"""Script that lists all <State> objects
from the database <hbtn_0e_6_usa>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model_state import Base, State


if __name__ == '__main__':
    """create engine
    """
    usr, pswd, dbname = sys.argv[1:4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(usr, pswd, dbname))

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State)

    for state in states:
        print("{}: {}".format(state.id, state.name))
