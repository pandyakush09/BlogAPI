from http.client import HTTPException
from fastapi import APIRouter, Depends, HTTPException
from .. import schemas, database, models
from  .. hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(
    tags=["Authentication"]
)

@router.post("/login")
def login(request : schemas.Login, db : Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Invalid Credentials")

    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=404, detail="Invalid Credentials")

    return user