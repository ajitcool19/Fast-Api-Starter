from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse


class AuthMiddleware(BaseHTTPMiddleware):

    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request, call_next):
        headers = request.headers
        auth = headers.get('Authorization')
        if not auth:
            return JSONResponse(status_code=401, content={"message": "Unauthorized"})

        return await call_next(request)