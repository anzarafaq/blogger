from __future__ import unicode_literals

import json

from render import render
from werkzeug import Request, Response, url_encode
from werkzeug.exceptions import HTTPException, NotFound, Unauthorized
from werkzeug.contrib.sessions import FilesystemSessionStore
from werkzeug.utils import redirect

#from blogger.data_models.users import authenticate as pw_auth
#from blogger.data_models.users import get_user_by_screen_name

from blogger.logger import logging
from blogger.cfg import cfg

logger = logging.getLogger(__name__)
session_store = FilesystemSessionStore('/tmp/sessions')


def user_info(req):
    user_id = req.values.get('user_id')
    user = get_user_by_screen_name(user_id)
    return Response(json.dumps({'pingid': False}))


def authenticate(user_id, passwd):
    if not pw_auth(user_id, passwd):
        return {"status": "Error: Username or Password Incorrect."}

    user = get_user_by_screen_name(user_id)
    if user:
    	return {"status": "Success"}
    else:
	return {"status": "Failed"}


def auth_check(f):
    '''
    Decorator to do basic auethentication checks.
    '''

    def wrapped(*args, **kwds):
        req = args[0]
        next_url = req.full_path
        if req.full_path in (None, '/?') :
            next_url =  '/'
        sid = req.cookies.get('session_id')
        if sid is None:
            return redirect('/login?next_url=%s' % next_url)
        else:
            session = session_store.get(sid)
            if session is None:
                return redirect('/login?next_url=%s' % next_url)
            if 'user_id' not in session:
                return redirect('/login?next_url=%s' % next_url)
            req.session = session

        return f(*args, **kwds)

    return wrapped


def logout(req):
    sid = req.cookies.get('session_id')
    if sid:
        session = session_store.get(sid)
        if 'user_id' in session: del (session['user_id'])
        session_store.save(session)
    return Response(render('signin.j2', next_url="/", login_form=True), mimetype='text/html')


def login(req):
    logger.info('processing login: next_url = %s', next_url)
    user_id = req.values.get('user_id')
    passwd = req.values.get('password')
    if user_id in (None, '') or passwd in (None, ''):
        return redirect('/login')
    sid = req.cookies.get('session_id')
    if sid is None:
        # First check that user exists...
        auth = authenticate(user_id, passwd)
        if auth and auth.get('status') == 'Success':
            req.session = session_store.new()
        else:
            return Response(render('login_failed.jinja2', error_message=auth.get('status')),
                            mimetype='text/html')
        req.session['user_id'] = user_id
        session_store.save(req.session)
        response = redirect('/')
        response.set_cookie('session_id', req.session.sid,
                            max_age=cfg.session_timeout,
                            secure=None, httponly=True)
        return response


def get_session_user_id(req):
    user_id = None
    sid = req.cookies.get('session_id')
    if sid is not None:
        store = session_store.get(sid)
        user_id = store.get('user_id')
    return user_id


def home(req):
    # Number of blogs shown
    rows = cfg.blog_page_count
    page = req.values.get('page', 0, type=int)
    
    user_id=get_session_user_id(req)
    blogs = get_blogs(rows=25, user_id=user_id) #Time sorted latest 25 blogs

    return Response(render('home.j2',
                           rows=rows,
                           page=page,
                           user_id=get_session_user_id(req)),
                    mimetype='text/html')
