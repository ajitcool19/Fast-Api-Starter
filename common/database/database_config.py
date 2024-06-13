from contextvars import ContextVar

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from common.config.config import current_config


def create_engine_based_on_env():

    return create_engine(
        current_config.SQLALCHEMY_DATABASE_URI,
        pool_size=20,
        max_overflow=160,
        pool_recycle=1
    )


engine = create_engine_based_on_env()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

db_session: ContextVar[Session] = ContextVar('db_session', default=Session(engine))

def get_db():
    db: Session = SessionLocal()
    create_tables() #  to be called if we want to create tables
    try:
        yield db
    except Exception:
        db.rollback()
    finally:
        db.close()

def context_aware_session():
    return db_session.get()


def create_tables():
    """
    create tables in the database
    """
    # just for development purposes
    # so just to make this clear - this is not an "unused import"
    # models must be imported before we call create_all method
    Base.metadata.create_all(bind=engine)
