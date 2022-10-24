from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from model.models import Desafiados
from DBConnection.database import engine, Base, get_db
from repository.repositories import DesafiadosRepository
from DBConnection.schemas import DesafiadosRequest, DesafiadosResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/api/desafiados", response_model=DesafiadosResponse, status_code=status.HTTP_201_CREATED)
def create(request: DesafiadosRequest, db: Session = Depends(get_db)):
    desafiado = DesafiadosRepository.save(db, Desafiados(**request.dict()))
    return DesafiadosResponse.from_orm(desafiado)


@app.get("/api/desafiados")
def read(db: Session = Depends(get_db)):
    desafiado = DesafiadosRepository.findAll(db)
    return [DesafiadosResponse.from_orm(desafiado) for desafiado in desafiado]


@app.put("/api/desafiados/{id}")
def update(id: int, request: DesafiadosRequest, db: Session = Depends(get_db)):
    if not DesafiadosRepository.existsId(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Desafiado not found"
        )
    desafiado = DesafiadosRepository.save(db, Desafiados(id=id, **request.dict()))
    return DesafiadosResponse.from_orm(desafiado)


@app.delete("/api/desafiados/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    if not DesafiadosRepository.existsId(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Desafiado not found"
        )
    DesafiadosRepository.delete(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)



