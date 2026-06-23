from fastapi import FastAPI

from viajei_api.schemas import Message

app = FastAPI()

@app.get('/', response_model=Message)
def ola_mundo():
    return{'Olá! Turma!','Buenos dias --gruop'}
