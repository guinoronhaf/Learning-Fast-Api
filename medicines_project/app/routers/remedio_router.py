from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.remedio_schema import (
        RemedioCreate,
        RemedioResponse,
        RemedioGetResponse
)
from services.remedio_service import RemedioService

router = APIRouter(prefix="/remedios")

@router.get(
        "/{remedio_id}",
        response_model=RemedioGetResponse
)
def get_remedio_by_id(remedio_id: int, db: Session = Depends(get_db)):
    return RemedioService.find_remedio_by_id(db, remedio_id)

@router.post(
        "/",
        response_model=RemedioResponse
)
def create_remedio(remedio: RemedioCreate, db: Session = Depends(get_db)):
    return RemedioService.create_remedio(db, remedio)
