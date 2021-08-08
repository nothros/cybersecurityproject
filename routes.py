from flask.globals import session
from app import app
from flask import redirect, render_template, request
from flask import render_template
import users, families

#DONE
@app.route("/")
def index():
    print(users.get_user())
    print(len(users.get_user()))
    if len(users.get_user()) < 2:
        return render_template("login.html", message="")
    else:
        family = families.get_family(session["user_id"])
        if family:
            familyname = families.get_familyname(family.family_id)
            username = session["user_name"]
            memberamount= families.get_amount(session["user_id"])
            return render_template("main.html", familyname=familyname, user_name=username, member_amount= memberamount)
        
        else:
            if session["user_role"]=="1":
                return render_template("add_family.html", message="")
            else:
                return render_template("join_family.html", message="")
         
    
#DONE
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
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
        if role != "1" and role != "2":
            return render_template("signup.html", message="Anna rooli")
        if users.register(username, name, password, role):
            return redirect("/")
        else:
            return render_template("signup.html", message="Käyttäjätunnus jo käytössä!")


@app.route("/nofamily", methods=["POST"])
def nofamily():
    name=request.form["familyname"]
    code=request.form["code"]
    if session["user_role"]=="1":
        if code == "":
            return render_template("add_family.html", message="Anna salasana!")
        if len(name) < 2 or len(name) > 30:
            return render_template("add_family.html", message="Nimen tulee olla 2-30 merkkiä")

        if families.add_family(name, code, session["user_id"]):
            familyname = name
            username = session["user_name"]
            memberamount= families.get_amount(session["user_id"])
            return render_template("main.html", familyname=familyname, user_name=username, member_amount= memberamount)
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
            memberamount= families.get_amount(session["user_id"])

            return render_template("main.html", familyname=familyname, user_name=username, member_amount= memberamount)
        else: 
            return render_template("join_family.html", message="Käyttäjätunnus käytössä!")

    return render_template("nofamily.html", message="väärin meni")



@app.route("/main", methods=["GET","POST"])
def mainpage():
    if request.method == "GET":
        return render_template("main.html", familyname=familyname, user_name=username, member_amount= memberamount)
    if request.method == "POST":
        return render_template("main.html")





#DONE
@app.route("/logout")
def logout():
    users.logout()
    return redirect("/") 
