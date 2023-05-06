#!/usr/bin/python3
""" Script that takes in the name of a state as an argument."""

import MySQLdb
import sys

if __name__ == "__main__":
    """Gather user input for MySQL credentials."""
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=password,
        db=db_name,
        port=3306)

    cursor = db.cursor()
    querty = "SELECT cities.name FROM cities \
              JOIN states ON cities.state_id = states.id \
              WHERE states.name = %s ORDER BY cities.id ASC;"
    cursor.execute(querty, (state,))
    rows = cursor.fetchall()
    if rows:
        print(", ".join(row[0] for row in rows))
    else:
        print()

    db.close()