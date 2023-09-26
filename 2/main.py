from fastapi import FastAPI
from pydantic import BaseModel
import pyjokes

class Joke(BaseModel):
    friend: str
    joke: str

class JokeInput(BaseModel):
    friend: str


app = FastAPI()


@app.get("/")
def joke():
    return pyjokes.get_joke()

@app.get("/{friend}")
def friend_joke(friend: str):
    return friend + " tells his joke: " + pyjokes.get_joke()

@app.post("/", response_model=Joke)
def create_joke(joke_input: JokeInput):
    """Создание шутки"""
    return Joke(friend=joke_input.friend, joke=pyjokes.get_joke)
