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

@router.get("/")
def get_remedio(db: Session = Depends(get_db)):
    all_remedios = [
            RemedioGetResponse(
                nome=remedio.nome,
                fabricante=remedio.fabricante,
                principio_ativo=remedio.principio_ativo
            )
            for remedio in RemedioService.find_all(db)
    ]

    return {
            "remedios": all_remedios
    }


@router.get(
        "/{remedio_id}",
        response_model=RemedioGetResponse
)
def get_remedio_by_id(remedio_id: int, db: Session = Depends(get_db)):
    return RemedioService.find_remedio_by_id(db, remedio_id)


@router.get(
        "/search/{remedio_nome}",
        response_model=RemedioGetResponse
)
def get_remedio_by_nome(remedio_nome: str, db: Session = Depends(get_db)):
    return RemedioService.find_remedio_by_nome(db, remedio_nome)


@router.post(
        "/",
        response_model=RemedioResponse
)
def create_remedio(remedio: RemedioCreate, db: Session = Depends(get_db)):
    return RemedioService.create_remedio(db, remedio)
