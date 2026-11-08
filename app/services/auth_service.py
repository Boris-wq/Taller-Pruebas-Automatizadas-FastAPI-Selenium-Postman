
from app.repositories.user_repository import UserRepository
from app.schemas.auth import LoginRequest


class AuthService:
    """Contiene la lógica de autenticación."""

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def authenticate(self, credentials: LoginRequest):
        """Verifica las credenciales del usuario."""

        user = self.repository.get_by_email(
            credentials.email
        )

        if not user:
            return None

        if user["password"] != credentials.password:
            return None

        return {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"]
        }
