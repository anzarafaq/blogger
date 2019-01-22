CREATE OR REPLACE FUNCTION update_row_modified_function_()
RETURNS TRIGGER
AS
$$
BEGIN
    -- ASSUMES the table has a column named exactly "row_modified_".
    -- Fetch date-time of actual current moment from clock, rather than start of statement or start of transaction.
    NEW.updated_at = clock_timestamp();
    RETURN NEW;
END;
$$
language 'plpgsql';
