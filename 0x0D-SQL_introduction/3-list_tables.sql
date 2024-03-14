-- List all tables in a dataBase
SELECT table_name
FROM information_schema.tables
WHERE table_schema = DATABASE();
