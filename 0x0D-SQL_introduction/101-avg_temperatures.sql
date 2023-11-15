-- import temperature.sql
mysql -u root -p -D hbtn_0c_0 < temperatures.sql
-- this does the logic
SELECT city, AVG(temperatures) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC