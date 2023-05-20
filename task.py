from fastapi import APIRouter, Path, Query, Body, HTTPException, status, File, UploadFile, Depends
from sqlalchemy.orm import Session
from typing_extensions import Annotated

import shutil

from models import Task, StatusType
from crud import get_task

from database import get_database_session


task_list=[

]

task_router = APIRouter()
task_list= []

@task_router.post("/files/")
# async def create_file(file: Annotated[bytes, File()]):
def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@task_router.post("/uploadfile/")
def create_upload_file(file: UploadFile, db: Session = Depends(get_database_session)):
    with open("img/destination.png", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}



@task_router.get("/", status_code=status.HTTP_200_OK)
def get(db: Session = Depends(get_database_session)):
    get_task(db,1)
    #records = db.query(Task).all()
    return { "tasks": task_list }

@task_router.post("/", status_code=status.HTTP_201_CREATED)  #status_code=201  status.HTTP_200_OK
def add(task: Task):
    # task_list.append({
    #     "task" : task.name,
    #     "status" : task.status,
    # })
    #verificamos que no este fuera de rango el indice
    if task in task_list:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task " + task.name +" already exist",
        )
    task_list.append(task)
    return { "tasks": status.HTTP_201_CREATED}

@task_router.put("/", status_code=status.HTTP_200_OK) #status_code=200
def update(index: int, task: Task):
    print(len(task_list))

    #verificamos que no este fuera de rango el indice
    if(len(task_list) <= index):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task ID doesn't exist",
        )

    task_list[index] = {
        "task" : task.name,
        "status" : task.status,
    }
    return { "tasks": task_list }

@task_router.get("/{index}", status_code=status.HTTP_200_OK) #status_code=200
def get(index: int):

    #verificamos que no este fuera de rango el indice
    if(len(task_list) <= index):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task ID doesn't exist",
        )

    return { "tasks": task_list[index] }

@task_router.delete("/", status_code=status.HTTP_200_OK) #status_code=200
def delete(index: int):
    del task_list[index] 
    return { "tasks": task_list }








@task_router.put("/product2/")
async def update_product(
    item: Task=
        Body(
            examples={
                "normalvv": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "convertedvv": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalidvv": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        ),
   
):
    results = { "item": item}
    return results



@task_router.put("/items/{item_id}")
async def update_item(item_id: int=Path(example=5), item: str= Query(example='testtt')):
    results = {"item_id": item_id, "item": item}
    return results





from typing_extensions import Annotated


@task_router.put("/product/")
async def update_product(
    item: Annotated[
        Task,
        Body(
            examples={
                "normalxx": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "convertedxx": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalidxx": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        ),
    ],
):
    results = { "item": item}
    return results