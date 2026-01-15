from pydantic import BaseModel

class ConsumoBase(BaseModel):
    data: str
    kwh: float
    custo: float
    observacao: str | None = None

class ConsumoCreate(ConsumoBase):
    pass

class Consumo(ConsumoBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class MetaResponse(BaseModel):
    meta: float

class MetaUpdateRequest(BaseModel):
    meta: float