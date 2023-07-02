from fastapi import FastAPI, Path, Query, Body, Depends, HTTPException, status, Header, Request
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session
from typing_extensions import Annotated

from task import task_router
from user import user_router
from database.database import get_database_session, Base, engine
from database.crud import getAll
from database.models import User, AccessToken




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
app.include_router(task_router, prefix="/tasks")
app.include_router(user_router)




# def validate_token(token: str = Header()):
#    if token != "TOKEN":
#       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,)



import time

from fastapi.responses import JSONResponse

# @app.middleware("http")
# async def add_middleware_here(request: Request, call_next):
#     token = request.headers["Authorization"]
#     try:
#         verification_of_token = verify_token(token)
#         if verification_of_token:
#             response = await call_next(request)
#             return response
#         else:
#             return JSONResponse(status_code=403) # or 401
#     except InvalidSignatureError as er:
#         return JSONResponse(status_code=401)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print("process_time")
    print(process_time)
    response.headers["X-Process-Time"] = str(process_time)
    return JSONResponse(status_code=401, content='No Authenticate')
    return response




API_KEY_TOKEN = "SECRET_PASSWORD"

api_key_header = APIKeyHeader(name="Token")

def protected_route(db: Session = Depends(get_database_session), token: str = Depends(api_key_header)):
    user = db.query(User).join(AccessToken).filter(AccessToken.access_token == token).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

@app.get("/get-task", dependencies=[Depends(protected_route)])
def protected_route(index: int):
   return {"hello": "FASTAPI"}

    # if token != API_KEY_TOKEN:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    # return {"hello": "fAPI_TOKENastapi"}


# async def authenticate(token: str = Depends(APIKeyHeader(name="Token"))):
#     if token != API_KEY_TOKEN:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
#     return token
    



# @app.get("/protected-route", dependencies=[Depends(api_token)])
# async def protected_route():
#     return {"hello": "world"}

# @app.get("/page/")
# def page(db: Session = Depends(get_database_session), dependencies=Depends(authenticate)):
#     print(getAll(db))
#     #create_user(db)
#     print(dependencies)
#     return {"page": 1}

# @app.get("/page2/")
# def page2(db: Session = Depends(get_database_session)):
#     get_task(db,1)
#     #create_user(db)
#     return {"page": 1}

@app.get("/pagetest/{page}")
def page(page: int = Path(...,gt=0), size: int = Query(12, le=100)):
    return {"page": page, "size": size}


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

from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates/")

@app.get("/")
async def index(request: Request, db: Session = Depends(get_database_session)):
    return templates.TemplateResponse("task/index.html", { "request": request, 'tasks': getAll(db) })