from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from database import get_db
from models import User
from auth_utils import verify_password, create_token

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/login/")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()

    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Credenciais inválidas")

    access_token = create_token({"sub": user.username})

    return {"access_token": access_token, "token_type": "bearer"}
