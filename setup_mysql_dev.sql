-- Creating a MySQL server database hbnb_dev_db:
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creating a new user in localhost with password hbnb_dev_pwd
CREATE USER
    IF NOT EXISTS 'hbnb_dev'@'localhost'
    IDENTIFIED BY 'hbnb_dev_pwd';

-- Granting user hbnb_dev privileges on database
GRANT ALL PRIVILEGES
    ON `hbnb_dev_db`.*
    TO'hbnb_dev'@'localhost'
    IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant SELECT priviledge to user on db performance_schema.
GRANT SELECT
    ON `performance_schema`.*
    TO 'hbnb_dev'@'localhost'
    IDENTIFIED BY 'hbnb_dev_pwd';
FLUSH PRIVILEGES;
