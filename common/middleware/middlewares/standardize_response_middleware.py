import json

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse


class StandardizeResponseMiddleWare(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):


        response = await call_next(request)
        response.headers["Content-Type"] = "application/json"

        response_body = [section async for section in response.__dict__['body_iterator']]
        response_content = b''.join(response_body).decode('utf-8')
        response_data = json.loads(response_content)

        response_data = {"data": response_data}

        response_data["status"] = response.status_code

        return JSONResponse(content=response_data)

