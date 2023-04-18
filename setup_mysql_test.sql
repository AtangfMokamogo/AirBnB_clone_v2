-- Creating a MySQL server database hbnb_test_db:
-- Grant SELECT priviledge to user on db performance_schema.
-- Grant user hbnb_test all privileges on hbnb_test_db
-- Creating a new user in localhost with password hbnb_test_pwd

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER
    IF NOT EXISTS 'hbnb_test'@'localhost'
    IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES
    ON `hbnb_test_db`.*
    TO'hbnb_test'@'localhost'
    IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT
    ON `performance_schema`.*
    TO 'hbnb_test'@'localhost'
    IDENTIFIED BY 'hbnb_test_pwd';
FLUSH PRIVILEGES;
