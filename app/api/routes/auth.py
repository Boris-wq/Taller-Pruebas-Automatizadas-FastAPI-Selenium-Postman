
from fastapi import APIRouter, HTTPException, status

from app.repositories.user_repository import user_repository
from app.schemas.auth import LoginRequest
from app.services.auth_service import AuthService


router = APIRouter(
    prefix="/api",
    tags=["Autenticación"]
)

auth_service = AuthService(user_repository)


@router.post("/login")
async def login(credentials: LoginRequest):

    user = auth_service.authenticate(credentials)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo o contraseña incorrectos"
        )

    return {
        "message": "Inicio de sesión exitoso",
        "user": user
    }
