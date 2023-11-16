-- subqueries
SELECT cities IN hbtn_0d_2 WHERE (SELECT * WHERE name = 'California' ORDER BY cities.id ASC)