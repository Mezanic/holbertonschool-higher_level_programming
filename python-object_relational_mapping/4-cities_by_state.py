#!/usr/bin/python3

"""Module that lists all the cities from the database hbtn_0e_4_usa

After connecting to MySQL server running on localhost
at port 3306 to access database hbtn_0e_4_usa,
it returns all the cities present in the DB.

Usage:
    python3 4-cities_by_state.py
    <mysql_username> <mysql_password> <database_name>

Args :
    mysql_username: argv[1]
    mysql_password: argv[2]
    database_name: argv[3]

Returns:
    Prints all the cities of DB sorted in ascending order
"""

import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )
    cursor = db.cursor()

    query = "SELECT cities.id, cities.name, states.name FROM cities JOIN \
        states ON cities.state_id = states.id ORDER BY cities.id ASC"
    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)
    cursor.close()
    db.close()
