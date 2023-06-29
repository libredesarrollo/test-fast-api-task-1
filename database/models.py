from sqlalchemy import Table
from sqlalchemy.schema import  Column, ForeignKey
from sqlalchemy.types import String, Integer, Text, Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database.database import Base

from schemas import StatusType


task_tag = Table('task_tag',
                 Base.metadata,
                    Column('task_id', Integer, ForeignKey('tasks.id'), primary_key=True),
                    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True))

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), unique=True)
    description = Column(Text())
    status = Column(Enum(StatusType))

    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), onupdate=func.now())

    category_id = Column(Integer, ForeignKey('categories.id'),
        nullable=False)
    
    user_id = Column(Integer, ForeignKey('users.id'),
        nullable=False)
    
    category = relationship('Category',lazy="joined", back_populates='tasks') #, backref='products'

    tags = relationship('Tag', secondary=task_tag)  #, back_populates='tasks'

    # status = Column(Enum(StatusTypeModel))
    # email = Column(String(30), unique=True)
    # website = Column(String(30))

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    # tasks = relationship('Task', back_populates='category',lazy="joined")

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    tasks = relationship('Task', back_populates='category',lazy="joined")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    surname = Column(String(20))
    email = Column(String(50))
    website = Column(String(50))
    hashed_password = Column(String(255))
    
class AccessToken(Base):
    __tablename__ = 'access_tokens'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    access_token = Column(String(255))
    expiration_date = Column(DateTime(timezone=True))
    class Config:
        orm_mode = True