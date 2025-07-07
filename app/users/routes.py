from app.users import services as user_services
from app.users.schemas import UserIn, UserOut
from fastapi import APIRouter, status

router = APIRouter(tags=["Usuários"])


@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserIn):
    return user_services.create_user(user_data)


@router.get("/", response_model=list[UserOut])
def get_users():
    return user_services.get_users()
