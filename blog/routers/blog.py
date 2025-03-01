from fastapi import APIRouter, Depends, status
from typing import List
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import blog


router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)
get_db = database.get_db

@router.get("/", response_model=List[schemas.ShowBlog])
def all(db : Session = Depends(get_db)):
    return blog.get_all(db)

##CREATE
@router.post("/", status_code = status.HTTP_201_CREATED)
def create(request: schemas.Blog, db : Session = Depends(get_db)):
    return blog.create(request, db)

##UPDATE
@router.put("/{id}", status_code = status.HTTP_202_ACCEPTED)
def update(id,request: schemas.Blog,db : Session = Depends(get_db)):
    return blog.update(id,request,db)


##DELETE
@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete(id,db : Session = Depends(get_db)):
    return blog.delete(id, db)


@router.get("/{id}", status_code = 200, response_model=schemas.ShowBlog)
def get_element(id, db : Session = Depends(get_db)):
    return blog.show(id , db)

