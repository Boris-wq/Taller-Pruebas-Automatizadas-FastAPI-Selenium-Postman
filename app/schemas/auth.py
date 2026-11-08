
from pydantic import BaseModel


class LoginRequest(BaseModel):
    """Datos necesarios para iniciar sesión."""

    email: str
    password: str
