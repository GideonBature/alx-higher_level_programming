#!/usr/bin/python3
"""a script <14-model_city_fetch_by_state.py> that
prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    usr, pswd, dbname = sys.argv[1:4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(usr, pswd, dbname))

    Session = sessionmaker(bind=engine)

    session = Session()

    cities_and_states = session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id).all()

    for city, state in cities_and_states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
