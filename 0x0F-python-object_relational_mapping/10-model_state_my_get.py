#!/usr/bin/python3
"""this is a function"""


def list_state_obj_with_name():
    """list state obj with name"""
    import sys
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    username = sys.argv[1]
    password = sys.argv[2]
    databasename = sys.argv[3]
    name = sys.argv[4]
    url = f'mysql://{username}:{password}@localhost:3306/{databasename}'
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    filter_name = session.query(State) \
        .filter(State.name == name).order_by(State.id).all()
    if filter_name:
        for fn in filter_name:
            print(fn.id)
    else:
        print('Not found')


if __name__ == "__main__":
    list_state_obj_with_name()
