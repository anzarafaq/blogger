from __future__ import unicode_literals

import json

from render import render
from werkzeug import Request, Response, url_encode

from blogger.web_app.data_models.blogs import get_blog

from blogger.logger import logging
from blogger.cfg import cfg


def get_blog(req):
    blog_id = req.values.get('blog_id', 0, type=int)
    blog = get_blog(blog_id=blog_id)  # Get blog by id

    return Response(json.dumps(blog, mimetype='text/html')


def get_blogs(req):
    user_id = get_session_user_id(req))
    blogs = get_blogs(user_id=user_id)  # Get blog by user id

    return Response(json.dumps(blogs, mimetype='text/html')


def add_blog(req):
    bloger_user_id = get_session_user_id(req))   # User id of source user
    blogged_to_userr_id = req.values.get('blogged_to')  # User id of the destination user
    
    blog = req.values.get('blog_text', '')    # Blog text sent by user

    # Persist the blog
    post_blog(src_user_id=bloger_user_id, target_user_id=blogged_to_userr_id, blog=blog)

    return Response(json.dumps({'status': 'SUCCESS'}), mimetype='text/html')
