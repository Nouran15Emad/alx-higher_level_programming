-- show the description of a table
SELECT column_name, column_type, character_maximum_length, is_nullable, column_default
FROM information_schema.columns
WHERE table_schema = '$1' AND table_name = 'first_table';
