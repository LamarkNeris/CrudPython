import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

from model.models import Funcionarios
from DBConnection.database import engine, Base, get_db
from repository.repositories import FuncionariosRepository
from DBConnection.schemas import FuncionariosRequest, FuncionariosResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)


@app.post("/api/funcionarios", response_model=FuncionariosResponse, status_code=status.HTTP_201_CREATED)
def create(request: FuncionariosRequest, db: Session = Depends(get_db)):
    funcionario = FuncionariosRepository.save(db, Funcionarios(**request.dict()))
    return FuncionariosResponse.from_orm(funcionario)


@app.get("/api/funcionarios")
def read(db: Session = Depends(get_db)):
    funcionario = FuncionariosRepository.findAll(db)
    return [FuncionariosResponse.from_orm(funcionario) for funcionario in funcionario]


@app.put("/api/funcionarios/{id}")
def update(id: int, request: FuncionariosRequest, db: Session = Depends(get_db)):
    if not FuncionariosRepository.existsId(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Funcionário not found"
        )
    funcionario = FuncionariosRepository.save(db, Funcionarios(id=id, **request.dict()))
    return FuncionariosResponse.from_orm(funcionario)


@app.delete("/api/funcionarios/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    if not FuncionariosRepository.existsId(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Funcionário not found"
        )
    FuncionariosRepository.delete(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
