-- subqueries
SELECT cities IN hbtn_0d_usa WHERE (SELECT * WHERE name = 'California' ORDER BY cities.id ASC)