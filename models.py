
from pydantic import BaseModel,  ValidationError, validator, Field, EmailStr, HttpUrl
from typing import List, Set, Optional
import enum 


from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text, Enum

from database import Base

class StatusType(str, enum.Enum):
    READY = "ready"
    PENDING = "pending"

# class StatusTypeModel(enum.Enum):
#     ready = 1
#     pending = 2

class TaskModel(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), unique=True)
    description = Column(Text())
    # status = Column(Enum(StatusTypeModel))
    status = Column(Enum(StatusType))
    # email = Column(String(30), unique=True)
    # website = Column(String(30))


class MyBaseModel(BaseModel):
    id: int
    @validator('id')
    def greater_than_zero(cls, v):
        if v <=0 :
            raise ValueError('must be greater than zero')
        return v
    
    @validator('id')
    def less_than_a_thousand(cls, v):
        if v >1000 :
            raise ValueError('must be less less than a thousand')
        return v
    
class User(MyBaseModel):
    id: int = Field(ge=5, le=120)
    name: str =  Field(..., min_length=3)
    surname: str
    email: EmailStr
    website: HttpUrl
    
class Category(MyBaseModel):
    id: int
    name: str
    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "id":55,
    #             "name": "Foo"
    #         }
    #     }
    # validaciones de nombre e email TODO

class Task(MyBaseModel):
    name: str
    description: Optional[str] = Field("No description", min_length=3)
    status: StatusType
    
    
    # user: User
    category: Category
    # tags: List[str] = []
    tags: Set[str] = set()
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id":55,
                "name": "Foo",
                "description": "A very nice Item",
                "status": StatusType.PENDING,
                "tags": ["tag 1"],
                "category": {
                    "id":66,
                    "name": "Foo"
                }
            }
        }

    
    @validator('name')
    def name_alphanumeric(cls, v):
        assert v.replace(" ", "").isalnum(), 'must be alphanumeric'
        return v
