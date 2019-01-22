import getpass

import bcrypt
import psycopg2.extras

from blogger.data_models.pgdb import conn, get_cursor
from blogger.logger import logging

logger = logging.getLogger(__name__)


def add_user_wrapper(screen_name, passwd):
    user_id = add_user(screen_name)
    hashed = bcrypt.hashpw(passwd, bcrypt.gensalt())
    store_passwd(user_id, hashed)
    return user_id


def add_user(screen_name):
    cur = get_cursor()
    sql = ('INSERT INTO blogger.users '
           '(screen_name) '
           'values (%s) '
           'RETURNING user_id')
    try:
        cur.execute(sql, (screen_name))
        conn.commit()
        user_id = cur.fetchone()[0]
        return user_id
    except Exception as ex:
        conn.rollback()
        raise ex


def get_user_by_screen_name(screen_name):
    sql = ('SELECT * FROM blogger.users '
           'WHERE screen_name = %s ')
    cur = get_cursor()
    cur.execute(sql, (screen_name,))
    user_row = cur.fetchone()
    return user_row


def get_user_by_id(user_id):
    sql = ('SELECT * FROM blogger.users '
           'WHERE user_id = %s ')
    cur = get_cursor()
    cur.execute(sql, (user_id,))
    user_row = cur.fetchone()
    return user_row


def get_users():
    sql = ('SELECT a.screen_name,'
           ' a.updated_at, a.created_at '
           'FROM blogger.users a '
           'order by screen_name')
    cur = get_cursor()
    cur.execute(sql)
    row = cur.fetchone()
    while row:
        yield row
        row = cur.fetchone()


def set_passwd_wrapper(args):
    return set_passwd(int(args.user_id))


def set_passwd(user_id):
    passwd = getpass.getpass()
    hashed = bcrypt.hashpw(passwd, bcrypt.gensalt())
    store_passwd(user_id, hashed)


def store_passwd(user_id, hashed):
    sql = ('UPDATE blogger.users '
           'SET passwd=%s '
           'WHERE user_id=%s')
    cur = conn.cursor()
    try:
        cur.execute(sql, (hashed, user_id))
        conn.commit()
    except Exception as ex:
        conn.rollback()
        raise ex


def list_users(args):
    sql = ('SELECT a.user_id, a.screen_name '
           'FROM blogger.users a '
           'order by screen_name')
    cur = get_cursor()
    cur.execute(sql)
    row =  cur.fetchone()
    while row:
        print row['user_id'], row['screen_name']
        row = cur.fetchone()


def get_all_users():
    sql = ('SELECT * FROM blogger.users order by screen_name')
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(sql)
    row =  cur.fetchone()
    while row:
        yield row
        row = cur.fetchone()


def authenticate(screen_name, passwd):
    user_row = get_user_by_screen_name(screen_name)
    if user_row and bcrypt.hashpw(passwd.encode('utf-8'), user_row['passwd'].encode('utf-8')) == user_row['passwd']:
        return True
    else:
        logger.warn("Failed login attempt by user %s", screen_name)
    return False


if __name__ == '__main__':
    import argparse

