from common.database.base_schema import Base


class UserLogin(Base):
    username : str
    password : str