from sqlalchemy.orm import Session

from models.remedio_model import RemedioModel
from schemas.remedio_schema import RemedioCreate

class RemedioRepository:

    @staticmethod
    def create_remedio(db: Session, remedio_data: RemedioCreate):
        remedio = RemedioModel(
                nome=remedio_data.nome,
                fabricante=remedio_data.fabricante,
                principio_ativo=remedio_data.principio_ativo
        )

        db.add(remedio)
        db.commit()
        db.refresh(remedio)

        return remedio


    @staticmethod
    def get_by_id(db: Session, id: int):
        return (
                db.query(RemedioModel)
                .filter(RemedioModel.id == id)
                .first()
        )

    @staticmethod
    def get_by_nome(db: Session, nome: str):
        return (
                db.query(RemedioModel)
                .filter(RemedioModel.nome == nome)
                .first()
        )
