
class UserRepository:
    """Gestiona el almacenamiento y consulta de usuarios."""

    def __init__(self):
        self.users = [
            {
                "id": 1,
                "name": "Administrador",
                "email": "admin@demo.com",
                "password": "Admin123"
            }
        ]

    def get_all(self):
        """Devuelve todos los usuarios."""
        return self.users

    def get_by_email(self, email: str):
        """Busca un usuario por su correo electrónico."""

        for user in self.users:
            if user["email"] == email:
                return user

        return None

    def create(self, user_data: dict):
        """Registra un usuario nuevo."""

        new_user = {
            "id": max(user["id"] for user in self.users) + 1,
            **user_data
        }

        self.users.append(new_user)

        return new_user

# Instancia compartida del repositorio
user_repository = UserRepository()
