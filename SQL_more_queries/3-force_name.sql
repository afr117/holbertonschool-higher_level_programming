-- Create the table force_name if it doesn't exist

USE hbtn_0d_2;
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);