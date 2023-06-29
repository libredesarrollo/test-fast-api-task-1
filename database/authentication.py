from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from database.password import verify_password
from database.models import User, AccessToken

from datetime import datetime, timedelta

from database.password import generate_token

def authenticate(email: str, password: str, db: Session): #-> Optional[UserDB]:
    user = db.query(User).filter(User.email == email).first()

    if user is None:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user


def create_access_token(user: User, db: Session) -> AccessToken:

    tomorrow = datetime.now() + timedelta(days=1)

    access_token = AccessToken(user_id=user.id, expiration_date=tomorrow, access_token=generate_token())

    db.add(access_token)
    db.commit()
    db.refresh(access_token)

    return access_token