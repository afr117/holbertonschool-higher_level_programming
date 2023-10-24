#!/usr/bin/python3
"""
This script connects to a MySQL server and retrieves states that match the user input.

Usage: ./2-my_filter_states.py <username> <password> <database> <state_name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id", (state_name,))
        results = cursor.fetchall()
        for row in results:
            print(row)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))

