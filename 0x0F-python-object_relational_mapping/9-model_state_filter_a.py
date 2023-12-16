#!/usr/bin/python3
"""this is a function"""


def list_state_obj_filter():
    """list all state obj that contain 'a'"""
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
    filter_a = session.query(State) \
        .filter(State.name.like('%a%')).order_by(State.id).all()
    for state in filter_a:
        print(f'{state.id}: {state.name}')


if __name__ == "__main__":
    list_state_obj_filter()
