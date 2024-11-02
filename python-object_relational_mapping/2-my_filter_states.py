#!/usr/bin/python3
"""
Module that retrieves a particular state name

After connecting to MySQL server running on localhost
at port 3306 to access database hbtn_0e_0_usa,
it returns the state name we search as fourth argument

Usage:
    python3 2-my_filter_states.py
    <mysql_username> <mysql_password> <database_name> <state_name_searched>

Args :
    mysql_username: argv[1]
    mysql_password: argv[2]
    database_name: argv[3]
    state_name_searched: argv[4]

Returns:
    Prints a particular state input as fourth argument using
    .format for the query
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """Main entry point"""

    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    state_name_searched = argv[4]

    with MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    ) as db:

        with db.cursor() as cursor:
            query = """SELECT * FROM states
                    WHERE name = '{:s}'
                    COLLATE utf8mb4_bin
                    ORDER BY states.id ASC""".format(argv[4])
            cursor.execute(query)

            states = cursor.fetchall()
            for state in states:
                print(state)
