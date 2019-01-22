DROP TABLE IF EXISTS blogger.blog_access CASCADE;
CREATE TABLE blogger.blog_access (
   access_id   serial PRIMARY KEY,
   blog_id          integer REFERENCES blogger.blogs (blog_id),   
   user_id          integer REFERENCES blogger.users (user_id), 
   status           integer DEFAULT 0,
   created_at       TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
   updated_at       TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
);

CREATE TRIGGER row_mod_on_access_rules_trigger_
BEFORE UPDATE
ON blogger.blog_access
FOR EACH ROW
EXECUTE PROCEDURE update_row_modified_function_();
