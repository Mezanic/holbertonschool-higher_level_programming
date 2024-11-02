#!/usr/bin/python3

""" lists all states that start with an N"""

import sys
import MySQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cursor = db.cursor()
    # execute query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for row in states:
        # Check for first letter N
        if row[1][0] == 'N':
            print(row)
    cursor.close()
    db.close()
