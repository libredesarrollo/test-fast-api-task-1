from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text, Enum

from database.database import Base

from schemas import StatusType

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), unique=True)
    description = Column(Text())
    status = Column(Enum(StatusType))
    # status = Column(Enum(StatusTypeModel))
    # email = Column(String(30), unique=True)
    # website = Column(String(30))


