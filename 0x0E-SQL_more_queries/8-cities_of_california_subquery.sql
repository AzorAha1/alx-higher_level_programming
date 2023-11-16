-- subqueries
SELECT id, name IN hbtn_0d_usa WHERE state_id = (SELECT id FROM states WHERE name = 'California' ORDER BY id ASC)