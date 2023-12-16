#!/usr/bin/python3
"""this is a function"""


def delete_obj_a():
    """delete obj a"""
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
    objs = session.query(State).filter(State.name.like('%a%')).all()
    for obj in objs:
        session.delete(obj)
    session.commit()


if __name__ == "__main__":
    delete_obj_a()
