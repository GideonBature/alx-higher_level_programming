#!/usr/bin/python3
"""a script that creates the <State> <“California”> with the
<City> <“San Francisco”> from the database hbtn_0e_100_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    usr, pswd, dbname = sys.argv[1:4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(usr, pswd, dbname))

    Base.metadata.create_all(engine)

    session = Session(engine)
    california = State(name="California", cities=[City(name="San Francisco")])

    session.add(california)

    session.commit()
