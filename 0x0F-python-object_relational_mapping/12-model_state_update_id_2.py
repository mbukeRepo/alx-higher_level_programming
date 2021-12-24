#!/usr/bin/python3
"""
  updates the row with id = 2
  Usage: ./12-model_state_update_id_2.py <mysql username> /
                                         <mysql password> /
                                         <database name>
"""

import sys
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()
