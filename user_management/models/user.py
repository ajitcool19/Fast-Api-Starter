from sqlalchemy import Column, Integer, VARCHAR, DateTime, Boolean

from common.database.database_config import Base


class User(Base):

    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True, index=True)
    name = Column('name', VARCHAR(50))
    email = Column('email', VARCHAR(50))
    password = Column('password', VARCHAR(50))
    status = Column('status', Integer)
    last_login = Column('last_login', DateTime)
