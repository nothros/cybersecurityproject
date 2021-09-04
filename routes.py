import datetime
import users
import families
import tasks
from flask import redirect, render_template, request, abort
from flask.globals import session
from app import app


@app.route("/")
def index():
    message = ""
    if not allow():
        return render_template("/login.html", message=message)
    if not families.user_have_family(session["user_id"]):
        if session["user_role"] == "aikuinen":
            return render_template("/add_family.html", message=message)
        return render_template("/join_family.html", message=message)

    familymembers = families.get_members(session["user_id"])
    today = datetime.date.today()
    all_tasks = tasks.get_tasks(session["user_id"], session["user_role"], today)
    count_done_tasks = tasks.count_today_done_tasks_by_user(session["user_id"], today)[0][0]

    return render_template("home.html",
                           message=message, familymembers=familymembers,
                           date=today, tasklist=all_tasks,
                           count_done_tasks=count_done_tasks)

#DONE
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if allow():
            redirect("/")
        return render_template("login.html", message="")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        login_value = users.login(username, password)
        if login_value and session["visible"]:
            return redirect("/")
        message = "Käyttäjätunnus tai salasana ei täsmää!"
        return render_template("login.html", message=message)

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
        message = "Täytä kaikki kentät oikein!"
        if (len(username) < 3 or len(username) > 15
                or len(name) < 2 or len(name) > 30
                or password == ""):
            return render_template("signup.html", message=message)
        if users.register(username, name, password, role):
            return redirect("/")
        message = "Käyttäjätunnus jo käytössä!"
        return render_template("signup.html", message=message)





@app.route("/nofamily", methods=["GET", "POST"])
def nofamily():
    if not allow() or families.user_have_family(session["user_id"]):
        return redirect("/")
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    name = request.form["familyname"]
    code = request.form["code"]
    if session["user_role"] == "aikuinen":
        if len(name) < 2 or len(name) > 30 or code == "":
            return render_template("add_family.html", message="Nimi tai salasana virheellinen!")
        if families.add_family(name, code, session["user_id"]):
            return redirect("/")
        return render_template("add_family.html", message="Nimi tai salasana virheellinen!")
    else:
        if len(name) < 2 or len(name) > 30 or code == "":
            return render_template("join_family.html", message="Nimi tai salasana virheellinen!")
        if families.join_family(name, code, session["user_id"]):
            return redirect("/")
        return render_template("join_family.html", message="Nimi tai salasana virheellinen!")


@app.route("/family", methods=["GET", "POST"])
def family():
    if not allow() or not families.user_have_family(session["user_id"]):
        return redirect("/")
    if request.method == "GET":
        familyname = families.get_familyname(session["user_id"])
        familymembers = families.get_members(session["user_id"])
        return render_template("family.html", familymembers=familymembers, familyname=familyname)

    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        remove_userid = int(request.form["delete"])
        if remove_userid == session["user_id"]:
            families.remove_family(session["user_id"])
            users.remove_user(session["user_id"])
            return redirect("/logout")
        users.remove_user(remove_userid)
        families.remove_familymember(remove_userid)
        familyname = families.get_familyname(session["user_id"])
        familymembers = families.get_members(session["user_id"])
        return render_template("family.html", familymembers=familymembers, familyname=familyname)


@app.route("/home", methods=["GET", "POST"])
def home():
    if not allow() or not families.user_have_family(session["user_id"]):
        return redirect("/")
    message = ""
    familymembers = families.get_members(session["user_id"])
    today = datetime.date.today()
    all_tasks = tasks.get_tasks(session["user_id"], session["user_role"], today)
    count_done_tasks = tasks.count_today_done_tasks_by_user(session["user_id"], today)[0][0]

    if request.method == "GET":
        return render_template("home.html",
                               message=message, familymembers=familymembers,
                               date=today, tasklist=all_tasks,
                               count_done_tasks=count_done_tasks)

    if request.method == "POST":
        if session["user_role"] == "aikuinen":
            if session["csrf_token"] != request.form["csrf_token"]:
                abort(403)
            task = request.form["task"]
            doer_id = request.form["doer"]
            deadline = request.form["deadline"]
            task_status = "tekemättä"
            if (task == "" or deadline == "" or len(task) > 20):
                message = "Syötä tehtävä(max.20 merkkiä) ja päivämäärä"
                count_done_tasks = tasks.count_all_done_tasks(session["user_id"], today)
                return render_template("home.html",
                                       message=message, familymembers=familymembers,
                                       date=today, tasklist=all_tasks,
                                       count_done_tasks=count_done_tasks)
            deadline2 = deadline+" 13:55:26"
            if datetime.datetime.strptime(deadline2, '%Y-%m-%d %H:%M:%S').date() < today:
                task_status = "myöhässä"
            tasks.add_task(task, session["user_id"], doer_id, deadline, task_status)
        else:
            done_task = request.form["update"]
            if session["csrf_token"] != request.form["csrf_token"]:
                abort(403)
            tasks.do_task(done_task)


        familymembers = families.get_members(session["user_id"])
        today = datetime.date.today()
        tasklist = tasks.get_tasks(session["user_id"], session["user_role"], today)
        count_done_tasks = tasks.count_today_done_tasks_by_user(session["user_id"], today)[0][0]
        return render_template("home.html",
                               message="", familymembers=familymembers,
                               date=today, tasklist=tasklist,
                               count_done_tasks=count_done_tasks)


@app.route("/tasklist", methods=["GET", "POST"])
def tasklist():
    if not allow() or not families.user_have_family(session["user_id"]):
        return redirect("/")
    if not allow() or not families.user_have_family(session["user_id"]):
        return redirect("/")
    if request.method == "GET":
        task_expired = tasks.get_status_if_late(session["user_id"])
        for task in task_expired:
            tasks.update_task_status_expired(task[0])
            all_tasks = tasks.get_tasks(session["user_id"], session["user_role"])
            done_tasks_count = tasks.count_all_tasks_by_status(session["user_id"], "tehty")[0][0]
            late_tasks_count = tasks.count_all_tasks_by_status(session["user_id"], "myöhässä")[0][0]
            all_tasks_count = tasks.count_all_tasks_by_status(session["user_id"], "tekemättä")[0][0] + late_tasks_count + done_tasks_count
            return render_template("tasklist.html",
                                tasklist=all_tasks, all_tasks_count=all_tasks_count,
                                late_tasks_count=late_tasks_count,
                                done_tasks_count=done_tasks_count)
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        removable_task_id = request.form["delete"]
        tasks.delete_task(removable_task_id)
    all_tasks = tasks.get_tasks(session["user_id"], session["user_role"])
    done_tasks_count = tasks.count_all_tasks_by_status(session["user_id"], "tehty")[0][0]
    late_tasks_count = tasks.count_all_tasks_by_status(session["user_id"], "myöhässä")[0][0]
    all_tasks_count = tasks.count_all_tasks_by_status(session["user_id"], "tekemättä")[0][0] + late_tasks_count + done_tasks_count
    return render_template("tasklist.html",
                           tasklist=all_tasks, all_tasks_count=all_tasks_count,
                           late_tasks_count=late_tasks_count,
                           done_tasks_count=done_tasks_count)



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
    return len(users.get_user()) > 2
