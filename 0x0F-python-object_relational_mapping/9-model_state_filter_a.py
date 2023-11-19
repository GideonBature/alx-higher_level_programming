#!/usr/bin/python3
"""script that lists all <State> objects that contain
the letter <a> from the database <hbtn_0e_6_usa>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model_state import Base, State


if __name__ == '__main__':
    """lists all state objects containing <a>
    """
    usr, pswd, dbname = sys.argv[1:4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(usr, pswd, dbname))

    Session = sessionmaker(bind=engine)

    session = Session()

    states_with_a = session.query(State).filter(State.name.like("%a%")).all()

    for state_with_a in states_with_a:
        print("{}: {}".format(state_with_a.id, state_with_a.name))
