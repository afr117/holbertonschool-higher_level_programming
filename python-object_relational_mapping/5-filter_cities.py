#!/usr/bin/python3
"""
This script lists all cities in a specified state from a MySQL database.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check and validate the command-line arguments
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database name> <state name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()

        # Execute SQL query to retrieve cities for the specified state
        cursor.execute("SELECT cities.name FROM cities " \
                       "INNER JOIN states ON cities.state_id = states.id " \
                       "WHERE states.name = %s " \
                       "ORDER BY cities.id", (state_name,))

        # Fetch all the results
        results = cursor.fetchall()

        # Format the cities as a comma-separated string
        cities = ", ".join(row[0] for row in results)

        # Display the result
        print(cities)

        # Close the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
