-- Creating a test database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creating a test user if it does not exist and assigning a password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Granting all privileges on the test database to the test user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Granting SELECT privileges on performance_schema (optional, depending on your needs)
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
