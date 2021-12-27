import datetime
import users
import infos
from flask import redirect, render_template, request, abort
from flask.globals import session
from app import app
from re import compile

# Code for pw/username checker https://github.com/lingthio/Flask-User/issues/198
PASSWORD_REGEX = compile(r'\A(?=\S*?\d)(?=\S*?[A-Z])(?=\S*?[a-z])\S{6,}\Z')
USERNAME_REGEX = compile(r'\A[\w\-\.]{3,}\Z')

def password_is_valid(password):
    return PASSWORD_REGEX.match(password) is not None

def username_is_valid(username):
    return USERNAME_REGEX.match(username) is not None

def check_auth(id):
    return session["user_id"]==id

#DONE
@app.route("/")
def index():
    #THIS IS REALLY UGLY SOLUTION, NEVER EVER USE THIS
    if len(users.get_user())>2:
        id = session["user_id"]
        info = infos.get_all(id)
        return render_template("profile.html", id = id, infos = info)
    else:
        message = ""
        return render_template("login.html", message=message)
#DONE
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            message = "Wrong username or password"
            return render_template("login.html", message=message)
    if request.method == "GET":
        return redirect("/")

#DONE
@app.route("/signup", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("signup.html", message="")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not username_is_valid(username) or not password_is_valid(password):
            message = "Use valid password(atleast 8 char A-Z, 0-9, a-z) and username(atleast 3 char)"
            return render_template("signup.html", message=message)
        if users.register(username, password):
            return redirect("/")
        else:
            message = "The Username is already in use"
            return render_template("signup.html", message=message)


@app.route("/profile/<id>", methods=["GET", "POST"])
def profile(id):
    #BROKEN ACCESS CONTROL
    info = infos.get_all(id)
    if request.method == "GET":
        return render_template("/profile.html", id = id, infos = info)


@app.route("/new", methods=["GET", "POST"])
def new():
    id = session["user_id"]
    info = infos.get_all(id)
    #AUTHENTICATION FAILURE
    if request.method == "POST":
        website = request.form["website"]
        username = request.form["username"]
        pw = request.form["pw"]
        infos.add_info(website, username, pw, id)
        info = infos.get_all(id)

        return render_template("/profile.html", id = id, infos = info)
    if request.method == "GET":
        return render_template("/profile.html", id = id, infos = info)

#DONE
@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    info=infos.get_info(id)
    if request.method == "POST":
        uname=request.form["new_username"]
        pw=request.form["new_pw"]
        if uname == "":
            uname = info[2]
        if pw == "":
            pw=info[3]
        infos.edit_info(id, uname, pw)
        return redirect("/")
    if request.method == "GET":
        return render_template("edit.html", info=info)

#DONE
@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")


