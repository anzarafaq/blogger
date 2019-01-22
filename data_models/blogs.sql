DROP TABLE IF EXISTS blogger.blogs CASCADE;

CREATE TABLE blogger.blogs (
  blog_id      serial PRIMARY KEY,
  title        varchar(64),
  blog_user_id integer REFERENCES blogger.users (user_id)
);

CREATE TRIGGER row_mod_on_blogs_trigger_
BEFORE UPDATE
ON blogger.blogs
FOR EACH ROW
EXECUTE PROCEDURE update_row_modified_function_();
