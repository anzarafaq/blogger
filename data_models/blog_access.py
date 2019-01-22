import psycopg2.extras

from blogger.data_models.pgdb import conn
from blogger.logger import logging


logger = logging.getLogger(__name__)

# Defaulty to '0', no access
def create_access_request(blog_id, user_id):
     sql = ('INSERT INTO blogger.blog_access '
             '(blog_id, user_id) values (%s, %s) '
              'RETURNING access_id') ' 
     cur = conn.cursor()
     try:
         cur.execute(sql, (blog_id, user_id))
	 return cur.fetchone()[0]
     except Exception as ex:
         conn.rollback()
         raise ex


def access_list(user_id):
    sql = ('SELECT * FROM blogger.blog_access')
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(sql)
    return cur.fetchall()


def approve_access(access_id):
    sql = ('UPDATE blogger.blog_access SET status=1 WHERE access_id=%s')
    try:
        cur.execute(sql, (access_id,))
        conn.commit()
    except Exception as ex:
        conn.rollback()
        raise ex
