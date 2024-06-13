from user_management.crud.user_crud import Crud
from user_management.models.user import User
from common.database.database_config import context_aware_session
from user_management.schema.create_user import CreateUser


class UserController:
    def __init__(self):
        self.crud = Crud(context_aware_session())

    def get_data(self, user_id):
        return self.crud.read(user_id)

    def create_data(self, create_user: CreateUser):
        user = User()
        user.name = create_user.name
        user.email = create_user.email
        user.password = create_user.password

        return self.crud.create(user)



