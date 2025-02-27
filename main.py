from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

@app.get("/blog") #basically in other api "/" are called endpoints but in FastAPI they are called "path"
def index(limit:int = 10 , published : bool = True , sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} Published Blogs from the DB'}
    else:
        return {'data': f'{limit}  Blogs from the DB'}

@app.get("/blog/unpublished")
def unpublished():
    return {"data" : "All Unpublished Blogs"}


@app.get("/blog/{id}") #get,put,post are called "Operation on Path"
def show(id:int): #This are called Path Operation Function
    return {'data':id}


@app.get("/blog/{id}/comment") #get,put,post are called "Operation on Path"
def comment(id): #This is called Path Operation Function
    return {'data':{'1','2'}}

class Blog(BaseModel):
    title: str
    body: str
    published : Optional[bool]

@app.post("/blog")
def create_blog(request: Blog):
    return {'data':f'Blog is Created with Title as {request.title}'}

