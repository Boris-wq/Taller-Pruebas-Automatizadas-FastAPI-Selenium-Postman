
from fastapi import APIRouter, HTTPException, status

from app.repositories.user_repository import user_repository
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService


router = APIRouter(
    prefix="/api/users",
    tags=["Usuarios"]
)

user_service = UserService(user_repository)


@router.get("/", response_model=list[UserResponse])
async def get_users():
    return user_service.get_users()


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_user(user_data: UserCreate):

    try:
        return user_service.create_user(user_data)

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error)
        )
