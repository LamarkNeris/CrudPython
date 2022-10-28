from sqlalchemy import Column, Integer, String

from DBConnection.database import Base


class Funcionarios(Base):
    __tablename__ = "funcionários"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(100), nullable=False)
    email: str = Column(String(200), nullable=False)
    function: str = Column(String(100), nullable=False)
