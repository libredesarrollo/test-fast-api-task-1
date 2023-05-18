from fastapi import FastAPI, Path, Query, Body, Depends
from task import task_router
from sqlalchemy.orm import Session

from typing_extensions import Annotated

from database import SessionLocal, Base, engine

from crud import get_task, create_user

Base.metadata.create_all(bind=engine)

def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

app = FastAPI()
app.include_router(task_router)


@app.get("/page/")
def page(db: Session = Depends(get_database_session)):
    get_task(db,1)
    create_user(db)
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