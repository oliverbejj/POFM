from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
app=FastAPI()

class Post(BaseModel):
    name: str 
    material: str 
    size: str
            
my_posts = []



@app.get("/posts")
async def get_posts():
    return {"data":my_posts}


@app.post("/posts")
async def user_input(post:Post):
    post_dict=post.dict()
    post_dict['id']=randrange(0,1000000)
    my_posts.append(post_dict)
    return {"data":"new post"}
# name str, material str, Size str