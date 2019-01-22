from flask import request

from blogger.endpoints.signin import register_user
from blogger.endpoints.signin import login as user_login
from blogger.endpoints.signin import logout as user_logout

from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__, template_folder='templates')


@app.route("/")
def index():
    return "Blogger API V0.1!"


@app.route("/users/register")
def register():
    register_user(request)


@app.route("/users/login")
def login():
    user_login(request)


@app.route("/users/logout")
def logout():
    user_logout(request)


"""
@app.route("/")
@app.route("/")
@app.route("/")
@app.route("/")
@app.route("/")
@app.route("/")
@app.route("/")
@app.route("/")
@app.route("/")
@app.route("/")
@app.route("/")
@app.route("/")
@app.route("/")
@app.route("/")
"""


@app.route("/hello/<string:name>/")
def hello(name):
    return render_template(
            'editor.html',name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
