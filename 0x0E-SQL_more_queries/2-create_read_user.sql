-- create database
CREATE database IF NOT EXISTS hbtn_0d_2;
-- create user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grant select priviledge
GRANT SELECT ON database.* to 'user_0d_2'@'localhost';