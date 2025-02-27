from sqlalchemy.orm import Session
from .. import models , schemas
from fastapi import HTTPException



def get_all(db : Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create( request: schemas.Blog ,db : Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(id:int, db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return "done"

def update(id:int, request: schemas.Blog ,db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).update(request.dict())
    db.commit()
    return "Updation Successful"

def show(id:int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog is None:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"error": "Blog not found"}
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog