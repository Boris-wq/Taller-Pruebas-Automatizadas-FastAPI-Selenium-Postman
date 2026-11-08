
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class UserService:
    """Contiene la lógica de negocio de los usuarios."""

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_users(self):
        """Obtiene todos los usuarios."""
        return self.repository.get_all()

    def create_user(self, user_data: UserCreate):
        """Valida y registra un usuario."""

        existing_user = self.repository.get_by_email(
            user_data.email
        )

        if existing_user:
            raise ValueError("El correo ya está registrado")

        new_user = user_data.model_dump()

        return self.repository.create(new_user)
