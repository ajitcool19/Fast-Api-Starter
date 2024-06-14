from common.database.database_config import Base
from sqlalchemy import Column, Integer, VARCHAR


class Student(Base):
    __tablename__ = 'students'

    id = Column('id', Integer, primary_key=True, index=True)
    name = Column('name', VARCHAR(50))
    age = Column('age', Integer)

