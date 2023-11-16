-- create user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- give priviledges
GRANT ALL on *.* to 'user_0d_1'@'localhost';
-- show grants
SHOW GRANTS FOR 'user_0d_1'@'localhost';
