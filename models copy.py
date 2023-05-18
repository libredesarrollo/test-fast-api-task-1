
from pydantic import BaseModel,  ValidationError, validator
from enum import Enum

class StatusType(str, Enum):
    READY = "ready"
    PENDING = "pending"

    
class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    
class Category(BaseModel):
    id: int
    name: str

    # validaciones de nombre e email TODO

class Task(BaseModel):
    id: int
    name: str
    description: str
    status: StatusType
    user: User
    category: Category
    
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
    
    @validator('name')
    def name_alphanumeric(cls, v):
        assert v.replace(" ", "").isalnum(), 'must be alphanumeric'
        return v
