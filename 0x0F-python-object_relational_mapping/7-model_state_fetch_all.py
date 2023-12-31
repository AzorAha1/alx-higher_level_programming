#!/usr/bin/python3
"""this is a function"""


def list_state_obj():
    """list all state objects"""
    import sys
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    username = sys.argv[1]
    password = sys.argv[2]
    databasename = sys.argv[3]
    url = f'mysql://{username}:{password}@localhost:3306/{databasename}'
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    allstates = session.query(State).order_by(State.id).all()
    for state in allstates:
        print(f'{state.id}: {state.name}')


if __name__ == "__main__":
    list_state_obj()
