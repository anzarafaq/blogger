from flask import request

from blogger.endpoints.signin import register_user
from blogger.endpoints.signin import login as user_login
from blogger.endpoints.signin import logout as user_logout

from blogger.endpoints.blogs_access import request_user_blog_post
from blogger.endpoints.blogs_access import access_requests
from blogger.endpoints.blogs_access import update_user_blog_access_request

from blogger.endpoints.blogs import get_blogs as user_blogs
from blogger.endpoints.blogs import get_blog as user_blog
from blogger.endpoints.blogs import user_blogs
from blogger.endpoints.blogs import create_user_blog

from blogger.endpoints.posts import create_user_blog_post
from blogger.endpoints.posts import user_blog_post
from blogger.endpoints.posts import delete_user_blog_post
from blogger.endpoints.posts import update_user_blog_post

from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__, template_folder='templates')


# Home
@app.route("/")
def index():
    return "Blogger API V0.1!"


# Register uesr
@app.route("/users/register")
def register():
    return register_user(request)


# Login
@app.route("/users/login")
def login():
    return user_login(request)


# Logout
@app.route("/users/logout")
def logout():
    return user_logout(request)


# Current logged in user requests for access to a certain blog
@app.route("/blogs/<blog_id>/access", methods=['UPDATE'])
def request__blog_access():
    return request_user_blog_post(request)


# List of requests for 'permissions' by other users
@app.route("/blogs/users/<user_id>/requests", methods=['UPDATE'])
def blog_access_requests():
    return access_requests(request)


# Approve an access request
@app.route("/blogs/users/<user_id>/requests/<reuest_id>/approve", methods=['UPDATE'])
def update_blog_access_request():
    return update_user_blog_access_request(request)


#Get blogs (top 25, for unsigned user)
@app.route("/blogs")
def blogs():
    return user_blogs(request)


# Get a specific blog by blog_id
@app.route("/blogs/<blog_id>")
def blog():
    return user_blog(request.get('blog_id'))


# Get all blogs for a user_id
@app.route("/blogs/users/<user_id>")
def userblogs():
    return user_blogs(request.get('user_id'))


# Create a blog
@app.route("/blogs/users/<user_id>", methods=['POST'])
def create_blog():
    return create_user_blog(request)


# Create a post, within a blog
@app.route("/blogs/<bog_id>/posts", methods=['POST'])
def create_post():
    return create_user_blog_post(request)


#Get a post by id
@app.route("/blogs/<blog_id>/posts/<post_id>")
def blog_post():
    return user_blog_post(request)


@app.route("/blogs/<bog_id>/posts/<post_id>", methods=['DELETE'])
def delete_blog_post():
    return delete_user_blog_post(request)


@app.route("/blogs/<bog_id>/posts/<post_id>", methods=['UPDATE'])
def update_blog_post():
    return update_user_blog_post(request)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
