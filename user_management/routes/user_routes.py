from fastapi import APIRouter

from user_management.controller.user_controller import UserController
from user_management.schema.create_user import CreateUser
from user_management.schema.user_login import UserLogin

router = APIRouter(prefix="/user")
controller = UserController()


@router.get("/{id}")
def read_root(id: int):
    return controller.get_data(id)

@router.post("/")
def create_data(create_user : CreateUser):
    return controller.create_data(create_user)

@router.post("/login")
def login(user_login: UserLogin):
    return controller.login(user_login)

