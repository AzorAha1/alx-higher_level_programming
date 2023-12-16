#!/usr/bin/python3
"""this is a function"""


def update_obj():
    """update state obj"""
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
    obj = session.query(State).filter(State.id == 2).first()
    obj.name = 'New Mexico'
    session.commit()


if __name__ == "__main__":
    update_obj()
