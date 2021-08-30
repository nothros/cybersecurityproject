from db import db

#DONE
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
            sql = "SELECT T.task, U.name, T.deadline, T.id, T.task_status FROM tasks T, users U WHERE U.id = T.doer_id AND creator_id=:creator_id AND deadline=:deadline ORDER BY T.done ASC"
            result = db.session.execute(sql, {"creator_id":user_id, "deadline":today})
            
            print(today)
        else:
            sql = "SELECT T.task, U.name, T.deadline, T.id, T.task_status FROM tasks T, users U WHERE U.id = T.doer_id AND creator_id=:creator_id ORDER BY T.deadline"
            result = db.session.execute(sql, {"creator_id":user_id})
        
        
        tasks = result.fetchall()
        print(tasks)
    if tasks == None:
        return False
    return tasks

def get_tasks_by_doer(doer_id):
    sql = "SELECT T.task, U.name, T.deadline, T.id, T.done, T.task_status FROM tasks T, users U WHERE U.id = T.doer_id AND doer_id=:doer_id ORDER BY T.deadline"
    result = db.session.execute(sql, {"doer_id":doer_id})
    tasks = result.fetchall()
    if tasks == None:
        return False
    return tasks

def get_tasks_by_date_and_doer(doer_id, today):
    sql = "SELECT T.task, U.name, T.deadline, T.id, T.done, T.task_status FROM tasks T, users U WHERE U.id = T.doer_id AND doer_id=:doer_id AND T.deadline=:deadline ORDER BY T.done ASC"
    result = db.session.execute(sql, {"doer_id":doer_id, "deadline":today})
    tasks = result.fetchall()
    if tasks == None:
        return False
    return tasks


def get_status_if_late(doer_id):
    sql = "SELECT T.id, T.task FROM tasks T, users U WHERE U.id = T.doer_id AND doer_id=:doer_id AND T.deadline < NOW() - INTERVAL '1 DAY'  AND done = false"
    result = db.session.execute(sql, {"doer_id":doer_id})
    tasks = result.fetchall()
    if tasks == None:
        return False
    return tasks




def update_task_status_expired(task_id):
    status='myöhässä'
    sql = "UPDATE tasks SET task_status=:status WHERE id=:id"
    db.session.execute(sql, {"status":status, "id":task_id})
    db.session.commit()


def delete_task(task_id):
    sql = "DELETE FROM tasks WHERE id=:id"
    db.session.execute(sql, {"id":task_id})
    db.session.commit()

def do_task(task_id):
    status = 'tehty'
    sql = "SELECT task_status FROM tasks WHERE id =:id"
    result=db.session.execute(sql, {"id":task_id})
    task_status = result.fetchone()
    print(task_status)
    if task_status[0]=='tehty':
        status = 'tekemättä'
    sql = "UPDATE tasks SET done = NOT done, task_status=:status WHERE id=:id"
    db.session.execute(sql, {"status":status, "id":task_id})
    db.session.commit()
