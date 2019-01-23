import psycopg2.extras

from blogger.data_models.pgdb import conn
from blogger.logger import logging

logger = logging.getLogger(__name__)


def create_blog(title, blog_user_id):
	sql = ('INSERT INTO blogger.blogs (title, blog_user_id) '
		' VALUES (%s, %s) RETURNING blog_id')
	cur = conn.cursor()
	try:
		cur.execute(sql, (title, blog_user_id))

	except Exception as ex:
		print "Ex: %s" % ex
		conn.rollback()
		raise ex

	conn.commit()
	blog_id = cur.fetchone()[0]
	return blog_id


def get_blog_by_id(blog_id):
    sql = ('SELECT * FROM blogger.blogs '
           'WHERE blog_id = %s ')
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(sql, (blog_id,))
    return cur.fetchall()



def get_blogs(rows=25, user_id):
    sql = ('SELECT * from blogger.blogs WHERE blog_user_id=%s'
           'ORDER BY blog_id '
           'limit %s ')
    cur = get_cursor()
    cur.execute(sql, (user_id, rows))
    return cur.fetchall()



