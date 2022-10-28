from sqlalchemy.orm import Session

from model.models import Funcionarios


class FuncionariosRepository:
    @staticmethod
    def findAll(db: Session) -> list[Funcionarios]:
        return db.query(Funcionarios).all()

    @staticmethod
    def save(db: Session, funcionarios: Funcionarios) -> Funcionarios:
        if funcionarios.id:
            db.merge(funcionarios)
        else:
            db.add(funcionarios)
        db.commit()
        return funcionarios

    @staticmethod
    def existsId(db: Session, id: int) -> bool:
        return db.query(Funcionarios).filter(Funcionarios.id == id).first() is not None

    @staticmethod
    def delete(db: Session, id: int) -> None:
        funcionario = db.query(Funcionarios).filter(Funcionarios.id == id).first()
        if funcionario is not None:
            db.delete(funcionario)
            db.commit()
