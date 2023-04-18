-- Creating a MySQL server database hbnb_dev_db:
-- Grant SELECT priviledge to user on db performance_schema.
-- Granting user hbnb_dev privileges on database
-- Creating a new user in localhost with password hbnb_dev_pwd

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER
    IF NO EXISTS 'hbnb_dev'@'localhost'
    IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES
    ON `hbnb_dev_db`.* TO
    'hbnb_dev'@'localhost'
    IDENTIFIED BY 'hbnb_dev_pwd';

GRANT SELECT PRIVILEGES
    ON `performance_schema`.*
    TO 'hbnb_dev'@'localhost'
    IDENTIFIED BY 'hbnb_dev_pwd';;
FLUSH PRIVILEGES;
