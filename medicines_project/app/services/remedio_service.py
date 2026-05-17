from sqlalchemy.orm import Session
from fastapi import HTTPException

from repositories.remedio_repository import RemedioRepository
from schemas.remedio_schema import RemedioCreate, RemedioGetResponse


class RemedioService:

    @staticmethod
    def create_remedio(db: Session, remedio_data: RemedioCreate):

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


    @staticmethod
    def find_all(db: Session):
        all_remedios = RemedioRepository.get_all(db)
        
        return all_remedios


    @staticmethod
    def find_remedio_by_id(db: Session, remedio_id: int):

        existing_remedio = RemedioRepository.get_by_id(
                db,
                remedio_id
        )

        if not existing_remedio:
            raise HTTPException(
                    status_code=401,
                    detail="Remédio não encontrado."
            )

        return RemedioGetResponse(
                nome=existing_remedio.nome,
                fabricante=existing_remedio.fabricante,
                principio_ativo=existing_remedio.principio_ativo
        )
