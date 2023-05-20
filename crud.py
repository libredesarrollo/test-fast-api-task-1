from sqlalchemy.orm import Session

from models import TaskModel, StatusType

def get_task(db: Session, task_id: int):
    print(db.query(TaskModel).filter(TaskModel.id == task_id).first().name)
    return db.query(TaskModel).filter(TaskModel.id == task_id).first()


def create_user(db: Session): #, user: Task
    # fake_hashed_password = user.password + "notreallyhashed"
    db_user = TaskModel(name="test 2", status=StatusType.PENDING,description='aaaaaaaa')
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user