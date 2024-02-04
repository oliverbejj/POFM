from fastapi import FastAPI, Request, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class Post(BaseModel):
    name: str
    material: str
    size: str


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to allow requests from specific origins
    allow_credentials=True,
    allow_methods=["*"],   # Adjust this to allow specific HTTP methods
    allow_headers=["*"],   # Adjust this to allow specific headers
)

app.mount("/static", StaticFiles(directory="static"), name="static")
my_posts=[]

@app.post("/posts")
def create_post(item: Post):
    my_posts.append(item.dict())
    return {"message": "received"}

@app.get("/posts")
def get_posts():
    return my_posts

@app.get("/")
def read_value(request: Request):
    value = "hello"
    return templates.TemplateResponse("index.html", {"request" : request, "value":value})




