-- Create user_0d_1 if not exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to user_0d_1 on all databases
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

--SELECT IFNULL(COUNT(*), 0) as user_exists
--FROM mysql.user
--WHERE User = 'user_0d_1';
