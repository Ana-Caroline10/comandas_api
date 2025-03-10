# Ana Caroline Silveira Felipe #
from pydantic import BaseModel

class Produto(BaseModel):
    id_produto: int = None
    nome: str
    descricao: str
    valor_unitario: float = None
    foto: bytes = None
    