-- prints the full description of the table - first_table
-- from the database gbtn_0c_0 in your MySQL server
-- Replace 'hbtn_0c_0' and 'first_table' with your database and table names
USE hbtn_0c_0;

SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, IS_NULLABLE, COLUMN_DEFAULT
FROM information_schema.COLUMNS
WHERE TABLE_NAME = 'first_table';
