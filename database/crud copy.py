from fastapi import Depends
from sqlalchemy.orm import Session

from database.models import Task, Category, StatusType

def getById(db: Session, task_id: int):
    print(db.query(Task).filter(Task.id == task_id).first().category.name)
    print(db.query(Category).filter(Category.id == 1).first().tasks[1].name)
    return db.query(Task).filter(Task.id == task_id).first()


def create(db: Session): #, user: Task
    # fake_hashed_password = user.password + "notreallyhashed"
    db_user = Task(name="test 2", status=StatusType.PENDING,description='aaaaaaaa', category_id=1, user_id=1)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

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


# async def get_post_or_404(
#     id: int = Depends(get_object_id),
#     database: AsyncIOMotorDatabase = Depends(get_database),
# ) -> PostDB:
#     raw_post = await database["posts"].find_one({"_id": id})
#     if raw_post is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
#     return PostDB(**raw_post)