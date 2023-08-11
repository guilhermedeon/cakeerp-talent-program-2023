from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from fastapi.openapi.utils import get_openapi
from models import Curso
from database import engine, Base, get_db
from repositories import CursoRepository
from schemas import CursoRequest, CursoResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

#Create
@app.post("/api/cursos", response_model=CursoResponse, status_code=status.HTTP_201_CREATED)
def create(request: CursoRequest, db: Session = Depends(get_db)):
    curso = CursoRepository.save(db, Curso(**request.dict()))
    return CursoResponse.from_orm(curso)

#Read all
@app.get("/api/cursos", response_model=list[CursoResponse])
def find_all(db: Session = Depends(get_db)):
    cursos = CursoRepository.find_all(db)
    return [CursoResponse.from_orm(curso) for curso in cursos]

#Read (by id)
@app.get("/api/cursos/{curso_id}",response_model=CursoResponse, status_code=status.HTTP_200_OK)
def find_by_id(db: Session = Depends(get_db), curso_id : int = None):
    curso = CursoRepository.find_by_id(db,curso_id)
    if curso == None:
        raise HTTPException(status_code=404, detail="Curso nao encontrado")
    return CursoResponse.from_orm(curso)

#Delete (by id)
@app.delete("/api/cursos/{curso_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(db: Session = Depends(get_db), curso_id : int = None):
    curso = CursoRepository.find_by_id(db,curso_id)
    if curso == None:
        raise HTTPException(status_code=404, detail="Curso nao encontrado")
    CursoRepository.delete_by_id(db,curso_id)

#Update (by id)
@app.put("/api/cursos/{curso_id}", response_model=CursoResponse, status_code=status.HTTP_200_OK)
def update_by_id(request: CursoRequest, db: Session = Depends(get_db), curso_id : int = None):
    curso = CursoRepository.find_by_id(db,curso_id)
    if curso == None:
        raise HTTPException(status_code=404, detail="Curso nao encontrado")
    curso = Curso(**request.dict())
    curso.id = curso_id
    curso = CursoRepository.save(db, curso)
    return CursoResponse.from_orm(curso)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Ambiente Virtual de Aprendizagem",
        version="1.0.0",
        summary="Alunos EAD",
        description="Sistema de Ambiente Virtual de Aprendizagem para auxiliar alunos 100% EAD",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
