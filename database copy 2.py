from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

<<<<<<< HEAD
DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/fastapi_task"
=======
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# DATABASE_URL = "mysql+mysqlconnector://root:root@localhost:3306/fastapi_task"
# DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/fastapi_task"
DATABASE_URL = "mysql+mysqlconnector://sail:password@localhost:3306/testing"
>>>>>>> f7242bc1319f07394e36daa31b6f1799f6af6f10
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