#!/usr/bin/python3
"""this is a class"""


from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class City(Base):
    """City model"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
