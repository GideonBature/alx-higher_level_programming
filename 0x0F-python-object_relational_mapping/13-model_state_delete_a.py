#!/usr/bin/python3
"""a script that deletes all <State> objects with a name
containing the letter <a> from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model_state import Base, State

if __name__ == '__main__':
    usr, pswd, dbname = sys.argv[1:4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(usr, pswd, dbname))

    Session = sessionmaker(bind=engine)

    session = Session()

    session.query(State).filter(State.name.like("%a%")).\
        delete(synchronize_session='fetch')

    session.commit()
