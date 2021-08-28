import datetime
import users
import families
import tasks
from flask import redirect, render_template, request
from flask.globals import session
from app import app


#DONE
@app.route("/")
def index():
    if not allow():
        print("JOO EI SOPII")
        return render_template("/login.html", message="")
    else:
        print("JOO SOPII")
        message = ""
        if families.user_have_family(session["user_id"]):
            familymembers = families.get_members(session["user_id"])
            today = datetime.date.today()
            tasklist = tasks.get_tasks(session["user_id"], session["user_role"], today)
            return render_template("home.html", message = "", familymembers=familymembers, date=today, tasklist=tasklist)
        else:
            if session["user_role"] == "aikuinen":
                return render_template("/add_family.html", message="")
            else:
                return render_template("/join_family.html", message="")

#DONE
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if allow():
            print("JOO SOPII")
            redirect("/")
        return render_template("login.html", message="")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        login_value = users.login(username, password)
        if login_value:
            return redirect("/")
        else:
            return render_template("login.html", message="Käyttäjätunnus tai salasana ei täsmää!")

#DONE
@app.route("/signup", methods=["GET", "POST"])
def register():
    if allow():
        redirect("/")
    if request.method == "GET":
        return render_template("signup.html", message="")

    if request.method == "POST":
        username = request.form["username"]
        name = request.form["name"]
        password = request.form["password"]
        role = request.form["role"]

        if len(username) < 3 or len(username) > 15:
            return render_template("signup.html",
                                  message="Käyttäjätunnuksessa tulee olla 3-15 merkkiä")
        if len(name) < 2 or len(name) > 30:
            return render_template("signup.html", message="Nimen tulee olla 2-30 merkkiä")
        if password == "":
            return render_template("signup.html", message="Anna salasana!")
        if role != "aikuinen" and role != "lapsi":
            return render_template("signup.html", message="Anna rooli")
        if users.register(username, name, password, role):
            return redirect("/")
        else:
            return render_template("signup.html", message="Käyttäjätunnus jo käytössä!")





@app.route("/nofamily", methods=["GET","POST"])
def nofamily():
    if not allow() or families.user_have_family(session["user_id"]):
        return redirect("/")
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    name = request.form["familyname"]
    code = request.form["code"]
    if session["user_role"] == "aikuinen":
        if len(name) < 2 or len(name) > 30 or code =="":
            return render_template("add_family.html", message="Nimi tai salasana virheellinen!")
        if families.add_family(name, code, session["user_id"]):
            return redirect("/")
        else:
            return render_template("add_family.html", message="Käyttäjätunnus käytössä!")
    else:
        if len(name) < 2 or len(name) > 30 or code =="":
            return render_template("join_family.html", message="Nimi tai salasana virheellinen!")
        if families.join_family(name, code, session["user_id"]):
            return redirect("/")
        else:
            return render_template("join_family.html", message="Nimi tai salasana virheellinen!")

    return redirect("/")


@app.route("/family", methods=["GET", "POST"])
def family():
    if not allow() or not families.user_have_family(session["user_id"]):
        return redirect("/")
    if request.method == "GET":

        familyname = families.get_familyname(session["user_id"])
        print(familyname)
        familymembers = families.get_members(session["user_id"])
        return render_template("family.html", familymembers=familymembers, familyname=familyname)
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        remove_userid = request.form["delete"]
        users.remove_user(remove_userid)

        familyname = families.get_familyname(session["user_id"])
        familymembers = families.get_members(session["user_id"])
        return render_template("family.html", familymembers=familymembers, familyname=familyname)


@app.route("/home", methods=["GET", "POST"])
def home():
    if not allow() or not families.user_have_family(session["user_id"]):
        return render_template('404.html'), 404
    message = ""
    familymembers = families.get_members(session["user_id"])
    today = datetime.date.today()
    tasklist = tasks.get_tasks(session["user_id"], session["user_role"], today)
    if request.method == "GET":
        return render_template("home.html", message = "", familymembers=familymembers, date=today, tasklist=tasklist)

    if request.method == "POST":
        if session["user_role"] == "aikuinen":
            if session["csrf_token"] != request.form["csrf_token"]:
                abort(403)
            task = request.form["task"]
            doer_id = request.form["doer"]
            deadline = request.form["deadline"]


            if (task == "" or deadline == ""):
                message = message +"Syötä tehtävä ja päivämäärä"
                return render_template("home.html", message = message, familymembers=familymembers, date=today, tasklist=tasklist)

            print(message)
            tasks.add_task(task, session["user_id"], doer_id, deadline)
        else:
            done_task = request.form["update"]
            if session["csrf_token"] != request.form["csrf_token"]:
                abort(403)
            tasks.do_task(done_task)


        familymembers = families.get_members(session["user_id"])
        today = datetime.date.today()
        tasklist = tasks.get_tasks(session["user_id"], session["user_role"], today)
        return render_template("home.html", message = "", familymembers=familymembers, date=today, tasklist=tasklist)


@app.route("/tasklist", methods=["GET", "POST"])
def tasklist():
    if not allow() or not families.user_have_family(session["user_id"]):
        return redirect("/")
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        removable_task_id = request.form["delete"]
        tasks.delete_task(removable_task_id)
    tasklist = tasks.get_tasks(session["user_id"], session["user_role"])
    return render_template("tasklist.html", tasklist=tasklist)










@app.route("/settings", methods=["GET", "POST"])
def settings():
    if not allow() or not families.user_have_family(session["user_id"]):
        return redirect("/")
    if request.method == "GET":
        return render_template("settings.html")











@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404




@app.route("/logout")
def logout():
    if not allow():
        return redirect("/")
    users.logout()
    return redirect("/")


def allow():
    print(len(users.get_user()) > 2)
    return len(users.get_user()) > 2
