
from pydantic import BaseModel,  ValidationError, validator, Field, EmailStr, HttpUrl
from typing import List, Set, Optional
from enum import Enum
from datetime import datetime

from fastapi import Form

def get_expiration_date(duration_seconds: int = 86400) -> datetime:
    return timezone.now() + timedelta(seconds=duration_seconds)

class StatusType(str,Enum):
    DONE = "done"
    PENDING = "pending"

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

class TaskSimple(MyBaseModel):
    name: str
    description: Optional[str] = Field("No description", min_length=3)
    status: StatusType    
    class Config:
        orm_mode = True



class TaskBase(BaseModel):
    name: str
    description: Optional[str] = Field("No description",min_length=5)
    status: StatusType
    
    category_id: int = Field(gt=0)
    class Config:
       orm_mode = True

    @classmethod
    def as_form(
            cls,
            name: str = Form(),
            description: str = Form(),
            status: str = Form(),
            category_id: str = Form(),
    ):
        return cls(name=name, description=description, status=status,category_id=category_id)

    
class TaskRead(TaskBase):
    id:int

class TaskWrite(TaskBase):
    id: Optional[int] = Field(default=None)
    user_id: Optional[int] = Field()
    @classmethod
    def as_form(
            cls,
            name: str = Form(),
            description: str = Form(),
            status: str = Form(),
            user_id: str = Form(),
            category_id: str = Form(),
    ):
        return cls(name=name, description=description, status=status,category_id=category_id, user_id=user_id, )

        
# class Task(MyBaseModel):
#     name: str
#     description: Optional[str] = Field("No description", min_length=3)
#     status: StatusType
    
#     # user: User
#     category: Category
#     # tags: List[str] = []
#     tags: Set[str] = set()
#     class Config:
#         orm_mode = True
#         schema_extra = {
#             "example": {
#                 "id":55,
#                 "name": "Foo",
#                 "description": "A very nice Item",
#                 "status": StatusType.PENDING,
#                 "tags": ["tag 1"],
#                 "category": {
#                     "id":66,
#                     "name": "Foo"
#                 }
#             }
#         }

#     @validator('name')
#     def name_alphanumeric(cls, v):
#         assert v.replace(" ", "").isalnum(), 'must be alphanumeric'
#         return v

class User(MyBaseModel):
    id: int = Field(ge=5, le=120)
    name: str =  Field(..., min_length=3)
    surname: str
    email: EmailStr
    website: HttpUrl
    class Config:
        orm_mode = True

# class UserBase(BaseModel):
#     email: EmailStr
#     class Config:
#         orm_mode = True
# class User(UserBase):
#     id: int
class UserCreate(User):
    password: str

class UserDB(User):
    hashed_password: str 

class AccessToken(MyBaseModel):
    user_id: int
    access_token: str
    expiration_date: datetime
    class Config:
        orm_mode = True