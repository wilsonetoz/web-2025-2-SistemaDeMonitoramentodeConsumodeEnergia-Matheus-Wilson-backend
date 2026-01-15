from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import RegisterRequest, TokenResponse
from auth_utils import hash_password, create_token

router = APIRouter(prefix="/register", tags=["Auth"])

@router.post("/", response_model=TokenResponse)
def register(data: RegisterRequest, db: Session = Depends(get_db)):

    exists = db.query(User).filter(
        (User.username == data.username) |
        (User.email == data.email)
    ).first()

    if exists:
        raise HTTPException(400, "Usuário ou email já existe")

    novo = User(
        username=data.username,
        email=data.email,
        hashed_password=hash_password(data.password)
    )

    db.add(novo)
    db.commit()
    db.refresh(novo)

    token = create_token({"sub": novo.username})

    return TokenResponse(access_token=token)
