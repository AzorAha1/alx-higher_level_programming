#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


username = sys.argv[1]
password = sys.argv[2]
databasename = sys.argv[3]
database_url = f'mysql://{username}:{password}@localhost:3306/{databasename}'
engine = create_engine(database_url)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
allstates = session.query(State).all()
for state in allstates:
    print(f'{state.id}: {state.name}')
