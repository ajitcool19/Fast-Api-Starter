from common.database.base_schema import Base


class CreateUser(Base):
    name: str
    email: str
    password: str
