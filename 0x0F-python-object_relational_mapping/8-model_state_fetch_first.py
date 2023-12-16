#!/usr/bin/python3
"""this is a function"""


def list_state_obj_first():
    """list first state object"""
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
    first = session.query(State).order_by(State.id).first()
    if first:
        print(f'{first.id}: {first.name}')
    else:
        print()


if __name__ == "__main__":
    list_state_obj_first()
