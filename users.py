from db import db
from app import app
from flask import session, abort, request
#from werkzeug.security import check_password_hash, generate_password_hash
import os
import secrets

def login(username,password):
    sql = "SELECT * FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None:
        return False
    else:
        if user.pword == password:
            session["user_id"] = user.id
            session["logged_in"] = True
            session["user_username"] = user.username
            # BROKEN AUTHENTICATION
            # XSS
            session["csrf_token"] = user.id
            return True
        else:
            return False

def get_user():
    return session

def register(username, password):
    #SENSITIVE DATA EXPOSURE
    try:
        sql = "INSERT INTO users (username, pword) VALUES (:username, :pword)"
        db.session.execute(sql, {"username":username, "pword":password})
        db.session.commit()
    except:
        return False
    return True
    
def logout():
    del session["user_id"]
    del session["logged_in"]
    del session["user_username"]
    del session["csrf_token"]