from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from auth_utils import get_current_user
from models import User
from schemas import MetaResponse, MetaUpdateRequest

router = APIRouter(prefix="/meta", tags=["Meta"])

@router.get("/", response_model=MetaResponse)
def get_meta(db: Session = Depends(get_db), token: str = Header()):
    user = get_current_user(token, db)
    return {"meta": user.meta}

@router.put("/", response_model=MetaResponse)
def update_meta(data: MetaUpdateRequest, db: Session = Depends(get_db), token: str = Header()):
    user = get_current_user(token, db)
    user.meta = data.meta
    db.commit()
    db.refresh(user)
    return {"meta": user.meta}
