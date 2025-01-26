DO $$ 
DECLARE
    table_name RECORD;
BEGIN
    -- Loop through all tables in the current schema
    FOR table_name IN
        SELECT tablename FROM pg_tables WHERE schemaname = 'public'
    LOOP
        -- Truncate the table and restart identity (reset AUTO_INCREMENT)
        EXECUTE FORMAT('TRUNCATE TABLE %I RESTART IDENTITY CASCADE', table_name.tablename);
    END LOOP;
END $$;
