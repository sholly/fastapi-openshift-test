import uvicorn
from enum import Enum
from fastapi import FastAPI


class PersonName(str, Enum):
    alex = "alex"
    bob = "bob"


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/people/{person_name}")
async def get_person(person_name: PersonName):
    if person_name == PersonName.alex:
        return {"description", "Its alex"}
    if person_name == PersonName.bob:
        return {"description", "Its BOB"}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
