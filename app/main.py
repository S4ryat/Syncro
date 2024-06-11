from typing import Any, List

from fastapi import FastAPI, HTTPException, Depends
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from app.actions import CRUDOperations
from app.db.database import get_db
from app.auth import get_current_username
from app.schemas import User

app = FastAPI(
    title="Music Recommendation API",
    description="API for Music Recommendation",
    version="1.0.0",
    # dependencies=[Depends(get_current_username)]
)


user_crud = CRUDOperations(User)
db = get_db()


@app.get("/")
def index():
    return {"message": "Hello world!"}


@app.get("/users", response_model=List[User], tags=["users"])
def list_users(skip: int = 0, limit: int = 100) -> Any:
    users = user_crud.get_all(db=db, skip=skip, limit=limit)
    return users


@app.post("/users", response_model=User, status_code=HTTP_201_CREATED, tags=["users"])
def create_user(body: User) -> Any:
    user = user_crud.create(db=db, obj_in=body)
    return user


@app.put(
    "/users/{id}",
    response_model=User,
    tags=["users"],
)
def update_user(*, id: int, user_in: User) -> Any:
    user = user_crud.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")
    user = user_crud.update(db=db, db_obj=user, obj_in=user_in)
    return user


@app.get(
    "/users/{id}",
    response_model=User,
    tags=["users"],
)
def get_user(*, id: int) -> Any:
    user = user_crud.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")
    return user


@app.delete(
    "/users/{id}",
    response_model=User,
    tags=["users"],
)
def delete_user(*, id: int) -> Any:
    user = user_crud.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")
    user = user_crud.remove(db=db, id=id)
    return user
