#!/usr/bin/python3
"""this is a function"""


def add_new_state_obj():
    """add new state obj"""
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
    newobj = State(name='Louisiana')
    session.add(newobj)
    session.commit()
    print(newobj.id)


if __name__ == "__main__":
    add_new_state_obj()
