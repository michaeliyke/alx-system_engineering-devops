-- Create database hbnb_test_db if not exists
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Using the new db
USE hbnb_test_db;

-- Creating the user hbnb_test
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Granting the privilege to use select on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Granting privileges on hbnb_test_db to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
