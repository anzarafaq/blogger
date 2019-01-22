import psycopg2
import psycopg2.extras

psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)


try:
    conn = psycopg2.connect("dbname='workday' user='workday' host='localhost' password='workday'")
    print "Got postgres db connection."
except:
    print "I am unable to connect to the database"
    raise


def get_cursor():
    return conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

