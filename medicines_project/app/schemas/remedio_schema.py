from pydantic import BaseModel

class RemedioCreate(BaseModel):
    nome: str
    fabricante: str
    principio_ativo: str

class RemedioResponse(BaseModel):
    id: int
    nome: str
    fabricante: str
    principio_ativo: str
