from common.database.base_schema import Base


class UserLogin(Base):
    email : str
    password : str
