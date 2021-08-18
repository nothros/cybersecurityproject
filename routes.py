from flask.globals import session
from app import app
from flask import redirect, render_template, request
from flask import render_template
import users, families
import datetime


#DONE
@app.route("/")
def index():
    if len(users.get_user()) < 2:
        return render_template("/login.html", message="")
    else:
        family = families.get_family(session["user_id"])
        if family:
            familymembers = families.get_members(session["user_id"])
            date = datetime.datetime.now()
            return render_template("home.html", familymembers=familymembers, date=date)

        else:
            if session["user_role"] == "aikuinen":
                return render_template("/add_family.html", message="")
            else:
                return render_template("/join_family.html", message="")
         
    
#DONE
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html",message="")
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        login_value = users.login(username, password)
        if login_value:
            return redirect("/")
        else:
            return render_template("login.html", message="Käyttäjätunnus tai salasana ei täsmää!")

#DONE
@app.route("/signup", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("signup.html", message="")
        
    if request.method == "POST":
        username = request.form["username"]
        name = request.form["name"]
        password = request.form["password"]
        role = request.form["role"]
        
        if len(username) < 3 or len(username) > 15:
            return render_template("signup.html", message="Käyttäjätunnuksessa tulee olla 3-15 merkkiä")
        if len(name) <2 or len(name)> 30:
            return render_template("signup.html", message="Nimen tulee olla 2-30 merkkiä")
        if password == "":
            return render_template("signup.html", message="Anna salasana!")
        if role != "aikuinen" and role != "lapsi":
            return render_template("signup.html", message="Anna rooli")
        if users.register(username, name, password, role):
            return redirect("/")
        else:
            return render_template("signup.html", message="Käyttäjätunnus jo käytössä!")





@app.route("/nofamily", methods=["POST"])
def nofamily():
    name = request.form["familyname"]
    code = request.form["code"]
    if session["user_role"]=="aikuinen":
        if code == "":
            return render_template("add_family.html", message="Anna salasana!")
        if len(name) < 2 or len(name) > 30:
            return render_template("add_family.html", message="Nimen tulee olla 2-30 merkkiä")

        if families.add_family(name, code, session["user_id"]):

            return redirect("/")
        else: 
            return render_template("add_family.html", message="Käyttäjätunnus käytössä!")
    else:
        if code == "":
            return render_template("join_family.html", message="Anna salasana!")
        if len(name) < 2 or len(name) > 30:
            return render_template("join_family.html", message="Nimen tulee olla 2-30 merkkiä")

        if families.join_family(name, code, session["user_id"]):
            familyname = name
            username = session["user_name"]
            memberamount = families.get_amount(session["user_id"])
            return redirect("/")
        else: 
            return render_template("join_family.html", message="Käyttäjätunnus käytössä!")

    return render_template("nofamily.html", message="väärin meni")






@app.route("/family", methods=["GET", "POST"])
def family():
    if request.method == "GET":
        familymembers = families.get_members(session["user_id"])
        return render_template("family.html", familymembers=familymembers)
    if request.method == "POST":
        remove_userid = request.form["delete"]
        users.remove_user(remove_userid)


        familymembers = families.get_members(session["user_id"])
        return render_template("family.html", familymembers=familymembers)


@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        familymembers = families.get_members(session["user_id"])
        date = datetime.datetime.now()
        return render_template("home.html", familymembers=familymembers, date=date)








#DONE
@app.route("/logout")
def logout():
    users.logout()
    return redirect("/") 
