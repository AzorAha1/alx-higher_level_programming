-- list number of records with the same score in table
SELECT score, number COUNT(*) FROM second_table GROUP BY score ORDER BY DESC;