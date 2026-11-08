
from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    """Datos necesarios para registrar un usuario."""

    name: str = Field(min_length=3, max_length=50)
    email: str
    password: str = Field(min_length=6)


class UserResponse(BaseModel):
    """Información pública que devolverá la API."""

    id: int
    name: str
    email: str
