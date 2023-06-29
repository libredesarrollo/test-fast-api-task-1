from sqlalchemy.orm import Session
from sqlalchemy.orm import load_only

from database.models import Task, Category, StatusType
from schemas import TaskSimple

from database.pagination import PageParams, paginate

def getById(db: Session, task_id: int):
    # print(db.query(Task).filter(Task.id == task_id).first().category.name)
    # print(db.query(Category).filter(Category.id == 1).first().tasks[1].name) 
    return db.query(Task).options(load_only(Task.name, Task.status)).get(task_id)
    return db.query(Task).filter(Task.id == task_id).first()
    

def getAll(db: Session):
    tasks = db.query(Task).all()
    return tasks 


def create(task: Task, db: Session):
    taskdb = Task(name=task.name, description=task.description, status=task.status, category_id = task.category_id, user_id = task.user_id)
    db.add(taskdb)
    db.commit()
    db.refresh(taskdb)
    return taskdb


def update(task: Task,db: Session): #, user: Task
    # fake_hashed_password = user.password + "notreallyhashed"
    task.name = 'aaaa'
    print(task.name)
    db.add(task, db)
    db.commit()
    db.refresh(task)
    return task

def delete(task: Task,db: Session):    
    db.delete(task)
    db.commit()

def pagination(db: Session, page:int, size:int):  
    pageParams = PageParams()
    return paginate(pageParams, db.query(Task).filter(Task.id > 1), TaskSimple)
    # db.query.paginate(models.Task,page,size)
