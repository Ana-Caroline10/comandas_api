import db
from sqlalchemy import Column, VARCHAR, Integer, FLOAT, LargeBinary

#ORM

class ProdutoDB(db.Base):
    __tablename__ = 'tb_produto'
    id_produto = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(200), nullable=False)
    descricao = Column(VARCHAR(200), nullable=False)
    valor_unitario = Column(FLOAT, nullable=False)
    foto = Column(LargeBinary, nullable=True)
    



    def __init__(self, id_produto, nome, descricao, valor_unitario, foto):
        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.valor_unitario = valor_unitario
        self.foto = foto
        