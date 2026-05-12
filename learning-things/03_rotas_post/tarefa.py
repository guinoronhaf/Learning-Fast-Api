from pydantic import BaseModel

class Tarefa(BaseModel):
    titulo: str # obrigatório
    descricao: str # obrigatório
    concluida: bool = False # opcional. Por padrão, False
