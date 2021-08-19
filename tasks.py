from db import db

def add_task(task, creator_id, doer_id, deadline):
    sql = "INSERT INTO tasks (task, creator_id, doer_id, deadline) VALUES (:task, :creator_id, :doer_id, :deadline)"
    db.session.execute(sql, {"task":task, "creator_id":creator_id, "doer_id":doer_id, "deadline":deadline})
    db.session.commit()

def get_tasks(user_id, role):
    if role != "aikuinen":
        tasks = get_tasks_by_doer(user_id)
    else:
        sql = "SELECT T.task, U.name, T.deadline, T.id FROM tasks T, users U WHERE U.id = T.doer_id AND creator_id=:creator_id ORDER BY T.deadline"
        result = db.session.execute(sql, {"creator_id":user_id})
        tasks = result.fetchall()
    if tasks == None:
        return False
    return tasks

def get_tasks_by_doer(doer_id):
    sql = "SELECT T.task, U.name, T.deadline, T.id, T.done FROM tasks T, users U WHERE U.id = T.doer_id AND doer_id=:doer_id ORDER BY T.deadline"
    result = db.session.execute(sql, {"doer_id":doer_id})
    tasks = result.fetchall()
    if tasks == None:
        return False
    return tasks


def delete_task(task_id):
        sql = "DELETE FROM tasks WHERE id=:id"
        db.session.execute(sql, {"id":task_id})
        db.session.commit()
