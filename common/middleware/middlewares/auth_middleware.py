import jwt
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from common.configs.config import current_config

class AuthMiddleware(BaseHTTPMiddleware):

    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request, call_next):

        if request.url.path == "/user/login":
            return await call_next(request)

        headers = request.headers
        auth = headers.get('Authorization')
        if not auth:
            return JSONResponse(status_code=401, content={"message": "Unauthorized"})
        else:
            if " " not in auth and len(auth.split(" ")) != 2:
                return JSONResponse(status_code=401, content={"message": "Unauthorized"})
            token = auth.split(" ")[1]

            jwt_payload = jwt.decode(token, current_config.JWT_SECRET, algorithms=["HS256"])

            if jwt_payload:
                email = jwt_payload.get("email")
                print(email)
                request.state.email = email
            else:
                return JSONResponse(status_code=401, content={"message": "Unauthorized"})


        return await call_next(request)