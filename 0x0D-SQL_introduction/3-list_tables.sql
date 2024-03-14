-- List all tables in a dataBase
USE information_schema;
SELECT table_name FROM tables
WHERE table_schema = 'mysql';
