from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from schemas import UserCreate
from database import password, models, database

from fastapi.security import OAuth2PasswordRequestForm

from database.authentication import authenticate, create_access_token

user_router = APIRouter()
@user_router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate, db: Session = Depends(database.get_database_session)) : # -> User
    hashed_password = password.get_password_hash(user.password)
    
    userdb = models.User(name=user.name, email=user.email, hashed_password=hashed_password, surname=user.surname, website=user.website )
    db.add(userdb)
    db.commit()
    db.refresh(userdb)

    return userdb

@user_router.post("/token")
async def create_token(
    form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm),
    db: Session = Depends(database.get_database_session)
):
    email = form_data.username
    password = form_data.password
    user =  authenticate(email, password, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    token =      create_access_token(user,db)
    return {"access_token": token.access_token}