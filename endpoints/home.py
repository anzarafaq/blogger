from __future__ import unicode_literals

import json

from render import render
from werkzeug import Request, Response, url_encode
from werkzeug.exceptions import HTTPException, NotFound, Unauthorized

from blogger.web_app.data_models.blogs import get_blogs

from blogger.logger import logging
from blogger.cfg import cfg


def home(req):
    # Number of blogs shown
    rows = cfg.blog_page_count
    page = req.values.get('page', 0, type=int)

    user_id=get_session_user_id(req))
    blogs = get_blogs(rows=25, user_id=user_id) #Time sorted latest 25 blogs

    return Response(render('home.j2',
                           rows=rows,
                           page=page,
                           user_id=get_session_user_id(req))
                    mimetype='text/html')
