-- Lists all the cities of California that can be found in the database 
SELECT cities.id, cities.name FROM hbtn_0d_usa
WHERE cities.state_id (SELECT id FROM states
WHERE name = "California" )
ORDER BY cities.id ASC;
