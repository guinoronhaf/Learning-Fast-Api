from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.remedio_schema import (
        RemedioCreate,
        RemedioResponse
)
from services.remedio_service import RemedioService

router = APIRouter(prefix="/remedios")

@router.post(
        "/",
        response_model=RemedioResponse
)
def create_user(remedio: RemedioCreate, db: Session = Depends(get_db)):
    return RemedioService.create_user(db, remedio)
