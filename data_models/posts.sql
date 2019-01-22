DROP TABLE IF EXISTS blogger.posts CASCADE;

CREATE TABLE blogger.posts (
  post_id      serial PRIMARY KEY,
  blog_id      integer REFERENCES blogger.blogs (blog_id),
  title        varchar(64),
  post_text    text
);

CREATE TRIGGER row_mod_on_posts_trigger_
BEFORE UPDATE
ON blogger.posts
FOR EACH ROW
EXECUTE PROCEDURE update_row_modified_function_();
