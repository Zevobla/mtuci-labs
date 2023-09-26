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
    return str(friend) + " tells his joke: " + pyjokes.get_joke()

@app.get("/multi/{friend}")
def multi_friend_joke(friend: str, jokes_number: int):
    result = ""
    for i in range(jokes_number):
        result +=  friend + f" tells his joke #{i+1}: " + pyjokes.get_joke()
    return result

@app.post("/", response_model=Joke)
def create_joke(joke_input: JokeInput):
    """Создание шутки"""
    return Joke(friend=str(joke_input.friend), joke=pyjokes.get_joke())
