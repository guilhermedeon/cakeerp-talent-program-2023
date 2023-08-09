'''
2. Criar um arquivo chamado database.py que realize a conexão a um banco de dados
SQLite.
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#URL/path do arquivo sqlite = ./sql_app.db
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
#engine principal
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread" : False}
)
#gera uma sessao do db
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#declaracao da base que sera utilizada no model
Base = declarative_base()
