from db import db
from werkzeug.security import check_password_hash, generate_password_hash

def add_family(name, code, user_id):
    hash_value = generate_password_hash(code)
    try: 
        sql = """INSERT INTO families (familyname, code) VALUES (:familyname, :code)"""
        db.session.execute(sql, {"familyname":name, "code":hash_value})
        db.session.commit()
    except:
        return False
        
    join_family(name, code, user_id)
    return True

def join_family(name, code, user_id):
    sql = "SELECT * FROM families WHERE familyname=:familyname"
    result = db.session.execute(sql, {"familyname":name})
    family = result.fetchone()
    if family == None:
        return False
    else:
        if check_password_hash(family.code, code):
            sql = """INSERT INTO familymembers (member_id, family_id)
                VALUES (:member_id, :family_id)"""
            db.session.execute(sql, {"member_id":user_id, "family_id":family.id})
            db.session.commit()
        else:
            return False
    return True

def user_have_family(memberid):
    sql = "SELECT id FROM familymembers WHERE member_id=:member_id"
    result = db.session.execute(sql, {"member_id":memberid})
    family = result.fetchone()
    if family == None:
        return False
    return True

def get_family(memberid):
    sql = "SELECT * FROM familymembers WHERE member_id=:member_id"
    result = db.session.execute(sql, {"member_id":memberid})
    family = result.fetchone()
    if family == None:
        return False
    return family

def get_familyname(familyid):
    sql = "SELECT * FROM families WHERE id=:id"
    result = db.session.execute(sql, {"id":familyid})
    family = result.fetchone()
    if family == None:
        return False
    return family.familyname

def get_members(userid):
    sql = "SELECT U.id, U.name, U.role FROM Users U, (SELECT * FROM familymembers WHERE member_id=:id) member1, familymembers member2 WHERE member1.family_id = member2.family_id AND  U.id = member2.member_id"
    result = db.session.execute(sql, {"id":userid})
    members = result.fetchall()
    return members