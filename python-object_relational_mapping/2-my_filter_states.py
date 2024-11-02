#!/usr/bin/python3

"""lists all states that have a specific name"""

import sys
import MySQLdb

looked_state = sys.argv[4]

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM states WHERE name = '{looked_state}' ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
    cursor.close()
    db.close()
