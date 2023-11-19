#!/usr/bin/python3
"""script that prints the first <State> object
from the database <hbtn_0e_6_usa>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model_state import Base, State


if __name__ == '__main__':
    """first state object
    """
    usr, pswd, dbname = sys.argv[1:4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(usr, pswd, dbname))

    Session = sessionmaker(bind=engine)

    session = Session()

    first_state = session.query(State).first()

    print("{}: {}".format(first_state.id, first_state.name))
