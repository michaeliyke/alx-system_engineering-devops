-- Create database hbnb_dev_db if not exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Using the new db
USE hbnb_dev_db;

-- Creating the user hbnb_dev
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Granting the privilege to use select on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Granting privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
