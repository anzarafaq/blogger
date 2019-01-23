import psycopg2.extras
from psycopg2 import IntegrityError

from blogger.data_models.pgdb import conn
from blogger.logger import logging

post_id      serial PRIMARY KEY,
  blog_id      integer REFERENCES blogger.blogs (blog_id),
  title        varchar(64),
  post_text    text


def create_post(blog_id, title, post_text):
	sql = ('INSERT INTO blogger.posts (blog_id, title, post_text) '
                ' VALUES (%s, %s, %s) RETURNING post_id')
        cur = conn.cursor()
        try:
                cur.execute(sql, (blog_id, title, post_text))

        except Exception as ex:
                print "Ex: %s" % ex
                conn.rollback()
                raise ex

        conn.commit()
        blog_id = cur.fetchone()[0]
        return blog_id


def get_posts_by_blogid(blog_id):
    sql = ('SELECT * FROM blogger.posts '
           'WHERE blog_id = %s ')
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(sql, (blog_id,))
    return cur.fetchall()


def get_post_by_id(post_id):
    sql = ('SELECT * FROM blogger.posts '
           'WHERE post_id = %s ')
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(sql, (post_id,))
    return cur.fetchall()

