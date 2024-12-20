#!/usr/bin/python3
"""
Module that takes the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa

After connecting to MySQL server running on localhost
at port 3306 to access database hbtn_0e_4_usa,
it returns all the cities of a defined state.

Usage:
    python3 5-filter_cities.py
    <mysql_username> <mysql_password> <database_name>

Args :
    mysql_username: argv[1]
    mysql_password: argv[2]
    database_name: argv[3]
    state_name: argv[4]

Returns:
    Prints all the cities of a defined state
    of the DB sorted in ascending order
"""
import MySQLdb
import sys

if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db.cursor()

    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    cities = cursor.fetchall()
    print(", ".join(city[0] for city in cities))

    cursor.close()
    db.close()
