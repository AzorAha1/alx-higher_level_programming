#!/usr/bin/python3
"""this is a function"""


def city_fetch_by_state():
    """city fetch by state"""
    import sys
    from sqlalchemy import create_engine
    from model_state import Base, State
    from model_city import City
    from sqlalchemy.orm import sessionmaker
    username = sys.argv[1]
    password = sys.argv[2]
    databasename = sys.argv[3]
    url = f'mysql://{username}:{password}@localhost:3306/{databasename}'
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    objs = session.query(State.name, City.id, City.name) \
        .join(State, State.id == City.state_id).order_by(City.id)
    for obj in objs:
        print(f'{obj[0]}: ({obj.id}) {obj.name}')


if __name__ == "__main__":
    city_fetch_by_state()
