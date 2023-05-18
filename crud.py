from sqlalchemy.orm import Session

from models import TaskModel, Task

def get_task(db: Session, task_id: int):
    return db.query(TaskModel).filter(TaskModel.id == task_id).first()


def create_user(db: Session):
    # fake_hashed_password = user.password + "notreallyhashed"
    db_user = TaskModel(name="test", email="teeeee",website='aaaaaaaa')
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user