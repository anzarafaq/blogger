DROP TABLE IF EXISTS blogger.users CASCADE;

CREATE TABLE blogger.users (
    user_id          serial PRIMARY KEY,
    created_at       TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at       TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    screen_name      varchar(64),  
    passwd           varchar(256),
);


CREATE TRIGGER row_mod_on_user_trigger_
BEFORE UPDATE
ON blogger.users 
FOR EACH ROW 
EXECUTE PROCEDURE update_row_modified_function_();
