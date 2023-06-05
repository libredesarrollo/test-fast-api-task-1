from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/fastapi_task"
# DATABASE_URL = "mysql+mysqlconnector://sail:password@localhost:3306/testing"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_database_session():
    print("********Init DB")
    try:
        db = SessionLocal()
        return db
    finally:
        print("********End app and DB")
        db.close()