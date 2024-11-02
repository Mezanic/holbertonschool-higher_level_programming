#!/usr/bin/python3

"""
A script that lists all states from the database hbtn_0e_0_usa where
the name matches the user-provided argument, safe from SQL injection.

The script takes four arguments:
1. MySQL username
2. MySQL password
3. Database name
4. State name to search for

Usage:
    ./3-my_safe_filter_states.py
    <mysql_username> <mysql_password> <database_name> <state_name>

The script connects to a MySQL server running on localhost at port 3306
and retrieves states with a name matching the user
input in ascending order by id.
"""

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
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (looked_state,))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
