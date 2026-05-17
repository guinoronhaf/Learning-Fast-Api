from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from core.database import Base

class RemedioModel(Base):
    __tablename__ = "remedio"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    fabricante: Mapped[str] = mapped_column(String(100), nullable=False)
    principio_ativo: Mapped[str | None] = mapped_column(String(100), nullable=True)
