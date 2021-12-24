#!/usr/bin/python3
"""
   connects to mysql database
   creates table and mapper class of State
   usage: ./6-model_state.py
                 <username>
                 <password>
                 <database>
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
