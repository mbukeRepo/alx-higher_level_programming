#!/usr/bin/python3
"""
  adds new state in the database
  adds new row in states table
  Usage: ./11-model_state_insert.py <mysql username> /
                                    <mysql password> /
                                    <database name>
                                    <state name searched>
"""

from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name="Louisiana")
    session.add(state)
    session.commit()
    print(state.id)
