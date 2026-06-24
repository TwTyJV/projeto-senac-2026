from http import HTTPStatus

from fastapi import FastAPI

from viajei_api.schemas.user import User, UserDB, UserPublic

app = FastAPI()

database = []


@app.get("/")
def read__root():
    return {"message": "Bem vindo!"}


@app.post("/auth/", status_code=HTTPStatus.CREATED, response_model=UserPublic)
def login(user: User):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id
