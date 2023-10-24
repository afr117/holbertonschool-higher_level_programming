#!/usr/bin/python3
"""
This script prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Set up the connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(engine)

    # Create a new Session
    session = Session()

    # Get the state object with the provided name
    state_name = sys.argv[4]
    result = session.query(State).filter(State.name == state_name).first()

    if result is not None:
        print(result.id)
    else:
        print("Not found")

    # Close the session
    session.close()

