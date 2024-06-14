from common.database.database_config import db_session, get_db, context_aware_session
from starlette.middleware.base import BaseHTTPMiddleware


class DbSessionMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request, call_next):
        print("request intercepted by db session middleware")

        db_session.set(next(get_db()))
        response = await call_next(request)
        # close connection after each call
        context_aware_session().close()
        return response
