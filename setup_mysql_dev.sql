-- Creating a database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creating a user if it does not exist and assigning a password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Granting all privileges on the database to the user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Granting SELECT privileges on performance_schema (optional, depending on your needs)
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
