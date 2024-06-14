import json

from fastapi import  Request
from starlette.middleware.base import BaseHTTPMiddleware
import jwt
from starlette.responses import JSONResponse

from common.configs.config import current_config
import datetime

class LoginMiddleware(BaseHTTPMiddleware):

    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response_body = [section async for section in response.__dict__['body_iterator']]
        response_content = b''.join(response_body).decode('utf-8')
        response_data = json.loads(response_content)
        if request.url.path == "/user/login" and response.status_code == 200:

            if response_data ["status"] == 200:
                # Generate a JWT token
                token = jwt.encode({"email":response_data["email"], "time_claim" : datetime.datetime.now().timestamp() +
                                    current_config.JWT_EXPIRATION_TIME
                                    }, current_config.JWT_SECRET, algorithm="HS256")
                # Attach the token to the response
                response_data['token'] = token
                return JSONResponse(content=response_data)

        return JSONResponse(content=response_data)
