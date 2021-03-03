--  creates the MySQL server user user_0d_1 and  give all privileges 
--  Create user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
-- Give all privilages
GRANT ALL PRIVILEGES ON *.* 
TO 'user_0d_1'@'localhost';
-- reload privilages
FLUSH PRIVILEGES;
