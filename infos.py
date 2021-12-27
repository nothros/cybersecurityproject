from db import db

def get_all(user_id):
    sql = """SELECT id, website, username, pw
                         FROM infos
                         WHERE users_id =:user_id"""
    result = db.session.execute(sql, {"user_id":user_id})
    infoes = result.fetchall()
    if infoes is None:
        return False
    return infoes

def add_info(website, username, pw, user_id):
    sql = """INSERT INTO infos
                 (website, username, pw, users_id)
                 VALUES (:website, :username, :pw, :users_id)"""
    db.session.execute(sql,
                       {"website":website, "username":username,
                        "pw":pw, "users_id":user_id})
    db.session.commit()

def get_info(info_id):
    sql = """SELECT id, website, username, pw
                         FROM infos
                         WHERE id =:info_id"""
    result = db.session.execute(sql, {"info_id":info_id})
    info = result.fetchall()[0]
    if info is None:
        return False
    return info

##INJECTION
def edit_info(info_id, username, pw):
    sql = "UPDATE infos SET username='" + username + "', pw='" + pw + "' WHERE id=" + info_id
    db.session.execute(sql)
    db.session.commit()