from db import db

def add_task(task, creator_id, doer_id, deadline):
    sql = "INSERT INTO tasks (task, creator_id, doer_id, deadline) VALUES (:task, :creator_id, :doer_id, :deadline)"
    db.session.execute(sql, {"task":task, "creator_id":creator_id, "doer_id":doer_id, "deadline":deadline})
    db.session.commit()

def get_tasks(user_id, role, today = 0):
    if role != "aikuinen":
        if today != 0:
            tasks = get_tasks_by_date_and_doer(user_id, today)
        else:
            tasks = get_tasks_by_doer(user_id)

    else:
        if today != 0:
            sql = "SELECT T.task, U.name, T.deadline, T.id FROM tasks T, users U WHERE U.id = T.doer_id AND creator_id=:creator_id AND deadline=:deadline"
            result = db.session.execute(sql, {"creator_id":user_id, "deadline":today})
            
            print(today)
        else:
            sql = "SELECT T.task, U.name, T.deadline, T.id FROM tasks T, users U WHERE U.id = T.doer_id AND creator_id=:creator_id ORDER BY T.deadline"
            result = db.session.execute(sql, {"creator_id":user_id})
        
        
        tasks = result.fetchall()
        print(tasks)
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

def get_tasks_by_date_and_doer(doer_id, today):
    sql = "SELECT T.task, U.name, T.deadline, T.id, T.done FROM tasks T, users U WHERE U.id = T.doer_id AND doer_id=:doer_id AND T.deadline=:deadline"
    result = db.session.execute(sql, {"doer_id":doer_id, "deadline":today})
    tasks = result.fetchall()
    if tasks == None:
        return False
    return tasks









def delete_task(task_id):
        sql = "DELETE FROM tasks WHERE id=:id"
        db.session.execute(sql, {"id":task_id})
        db.session.commit()

def do_task(task_id):
        sql = "UPDATE tasks SET done = NOT done WHERE id=:id"
        db.session.execute(sql, {"id":task_id})
        db.session.commit()
