#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Engine yaradılır
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Session yaradılır
    Session = sessionmaker(bind=engine)
    session = Session()

    # Adında 'a' hərfi olan bütün ştatları tapırıq
    states = session.query(State).filter(State.name.like('%a%')).all()

    # Hər birini silirik
    for state in states:
        session.delete(state)

    # Dəyişiklikləri commit edirik
    session.commit()

    # Sessiyanı bağlayırıq
    session.close()
