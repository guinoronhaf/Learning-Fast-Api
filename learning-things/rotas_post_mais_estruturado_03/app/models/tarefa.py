from pydantic import BaseModel, Field
from datetime import datetime

class Tarefa(BaseModel):
    titulo: str = Field(min_length=3)
    descricao: str
    concluida: bool = False
    prioridade: str = "média"
    data_criacao: datetime = Field(default_factory=datetime.now)
