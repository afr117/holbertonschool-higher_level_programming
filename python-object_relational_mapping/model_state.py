#!/usr/bin/python3
"""
This module defines a State class.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class with attributes id and name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)

    def __str__(self):
        """Return a string representation of the State object."""
        return self.name

