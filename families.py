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
    
def get_amount(memberid):
    sql = "SELECT COUNT(t2.family_id) FROM familymembers t1 JOIN familymembers t2 ON t2.family_id = t1.family_id WHERE t1.member_id =:member_id GROUP BY t1.member_id"
    result = db.session.execute(sql, {"member_id":memberid})
    counter = result.fetchone()[0]
    return counter

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