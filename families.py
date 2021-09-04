from db import db
from werkzeug.security import check_password_hash, generate_password_hash

def add_family(name, code, user_id):
    hash_value = generate_password_hash(code)
    try:
        sql = "INSERT INTO families (familyname, code) VALUES (:familyname, :code)"
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
    if family is None:
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

def remove_family(memberid):
    sql = """DELETE FROM families
                 USING familymembers
                 WHERE familymembers.member_id =:memberid
                 AND familymembers.family_id = families.id"""
    db.session.execute(sql, {"memberid":memberid})
    db.session.commit()

def remove_familymember(memberid):
    sql = "DELETE FROM familymembers WHERE member_id =:memberid"
    db.session.execute(sql, {"memberid":memberid})
    db.session.commit()

def user_have_family(memberid):
    sql = """SELECT fm.id
                 FROM familymembers fm, families f
                 WHERE fm.member_id=:member_id
                 AND f.visible = true
                 AND f.id = fm.family_id"""
    result = db.session.execute(sql, {"member_id":memberid})
    family = result.fetchone()
    if family is None:
        return False
    return True

def get_family(memberid):
    sql = """SELECT * FROM familymembers WHERE member_id=:member_id"""
    result = db.session.execute(sql, {"member_id":memberid})
    family = result.fetchone()
    if family is None:
        return False
    return family

def get_familyname(memberid):
    sql = """SELECT F.familyname
                 FROM families F, familymembers M
                 WHERE F.id = M.family_id
                 AND M.member_id =:memberid"""
    result = db.session.execute(sql, {"memberid":memberid})
    familyname = result.fetchone()
    if familyname is None:
        return False
    return familyname[0]

def get_members(userid):
    sql = """SELECT U.id, U.name, U.role
             FROM users U, (SELECT * FROM familymembers WHERE member_id=:id) member1, familymembers member2
             WHERE member1.family_id = member2.family_id
             AND  U.id = member2.member_id"""
    result = db.session.execute(sql, {"id":userid})
    members = result.fetchall()
    return members
