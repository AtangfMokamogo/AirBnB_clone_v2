-- Creating a MySQL server database hbnb_test_db:
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creating a new user in localhost with password hbnb_test_pwd
CREATE USER
    IF NOT EXISTS 'hbnb_test'@'localhost'
    IDENTIFIED BY 'hbnb_test_pwd';

-- Granting user hbnb_test privileges on database
GRANT ALL PRIVILEGES
    ON `hbnb_test_db`.*
    TO'hbnb_test'@'localhost';

-- Grant SELECT priviledge to user on db performance_schema.
GRANT SELECT
    ON `performance_schema`.*
    TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
