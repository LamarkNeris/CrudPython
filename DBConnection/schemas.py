from pydantic import BaseModel


class FuncionariosBase(BaseModel):
    name: str
    email: str
    function: str


class FuncionariosRequest(FuncionariosBase):
    ...


class FuncionariosResponse(FuncionariosBase):
    id: int

    class Config:
        orm_mode = True



