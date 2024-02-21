from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
import requests



app = FastAPI()

'''
how to run it in console :
uvicorn fast_api:app --reload

how to access swagger docs: 
http://localhost:8000/docs

'''

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    name: str
    description: str 
    price: float
    tax: float 


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.post("/items/")
async def create_item(item: Item):
    return item

@app.get("/pokemon")
async def pull_pokemon():
    headers = {'Accept': 'application/json'}
    r = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151%27', headers=headers)
    print(f"Response: {r.json()}")
    return r.json()