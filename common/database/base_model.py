import datetime
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy import inspect

from common.database.database_config import Base, context_aware_session


class BaseModel(Base):
    __abstract__ = True

    now = lambda: datetime.datetime.now().replace(microsecond=0)
    created_date = Column('FLD_CREATED_DATE', DateTime, default=now)
    modified_date = Column('FLD_MODIFIED_DATE', DateTime, default=now, onupdate=now)

    def save(self, update=False):

        """
        Try to avoid using this method, it's just handy for test cases
        """

        session = self.get_session()
        if not session:
            session = context_aware_session()
        session.add(self)
        try:
            session.commit()
        except Exception:
            session.rollback()
            raise
        return self

    def update(self, values: dict) -> None:
        """
        update the attributes to model only
        """
        if isinstance(values, dict):
            for key, value in values.items():
                setattr(self, key, value)

        elif hasattr(values, '__dict__'):
            for key, value in values.__dict__.items():
                setattr(self, key, value)

    def get_session(self):
        return inspect(self).session

    def __str__(self):
        filtered_dict = {}
        for key, val in vars(self).items():
            if not key.startswith('_'):
                filtered_dict[key] = val
        return f'{self.__class__.__name__} {str(filtered_dict)}'
