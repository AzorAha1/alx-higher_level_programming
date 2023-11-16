-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use hbtn_0d_usa database
USE hbtn_0d_usa;
-- create table with stateid being a foreign key that references the id of the states table
CREATE TABLE IF NOT EXISTS cities(id INT PRIMARY KEY AUTO_INCREMENT, state_id INT NOT NULL, FOREIGN KEY(state_id) REFERENCES states(id));
