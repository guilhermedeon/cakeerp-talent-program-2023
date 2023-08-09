'''
3. Criar um arquivo chamado models.py onde contenha um modelo de estrutura de uma tabela
para o banco de dados com nome de "users" com as seguintes colunas:
a. id: int
b. name: string
c. email: string
d. description: string
'''

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    description = Column(String, index=True)
