from db import db
from flask import session, abort, request
from werkzeug.security import check_password_hash, generate_password_hash
import os
import secrets

def login(username,password):
    sql = "SELECT * FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["user_username"] = user.username
            session["user_role"] = user.role
            session["user_name"] = user.name
            session["csrf_token"] = secrets.token_hex(16)
            return True
        else:
            return False

def get_user():
    return session


def register(username, name, password, role):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, name, password, role) VALUES (:username, :name, :password,:role)"
        db.session.execute(sql, {"username":username, "name":name, "password":hash_value, "role":role})
        db.session.commit()
    
    except: 
        return False

    return True

def remove_user(userid):
        sql = "DELETE FROM users WHERE id=:id"
        db.session.execute(sql, {"id":userid})
        db.session.commit()
    
def logout():
    del session["user_id"]
    del session["user_username"]
    del session["user_role"]
    del session["user_name"]
    del session["csrf_token"]