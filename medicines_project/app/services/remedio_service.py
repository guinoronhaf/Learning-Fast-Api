from sqlalchemy.orm import Session
from fastapi import HTTPException

from repositories.remedio_repository import RemedioRepository
from schemas.remedio_schema import RemedioCreate


class RemedioService:

    @staticmethod
    def create_user(db: Session, remedio_data: RemedioCreate):

        existing_remedio = RemedioRepository.get_by_nome(
                db,
                remedio_data.nome
        )

        if existing_remedio:
            raise HTTPException(
                    status_code=400,
                    detail="Remédio já cadastrado."
            )

        return RemedioRepository.create_remedio(db, remedio_data)
