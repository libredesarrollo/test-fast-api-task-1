from fastapi import FastAPI, Path, Query, Body, Depends
from sqlalchemy.orm import Session
from typing_extensions import Annotated

from task import task_router
from database.database import get_database_session, Base, engine
from database.crud import get_task, create_user
from database.models import Task

# task = Task()
Base.metadata.create_all(bind=engine)

# def get_database_session():
#     print("********Init DB")
#     try:
#         db = SessionLocal()
#         return db
#     finally:
#         print("********End app and DB")
#         db.close()


app = FastAPI()
app.include_router(task_router)


@app.get("/page/")
def page(db: Session = Depends(get_database_session)):
    #get_task(db,1)
    #create_user(db)
    return {"page": 1}

@app.get("/page2/")
def page2(db: Session = Depends(get_database_session)):
    get_task(db,1)
    #create_user(db)
    return {"page": 1}

# @app.get("/page/")
# def page(page: int = Path(gt=0), size: int = Query(10, le=100)):
#     return {"page": page, "size": size}


# @app.post("/products")
# async def product_example(
#     product: str = 
#         Body(
#             examples={
#                 "normal":{
#                     {
#                         "name": "Ps5",
#                         "description": "Game Console",
#                         "price": 599,
#                     },
#                 },
#                 "other":{
#                     {
#                         "name": "Xbox S",
#                         "description": "Game Console",
#                         "price": 499,
#                     },
#                 }
#             }
#         ),
  
# ):
#     return {"product": product}