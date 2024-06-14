from datetime import datetime

from starlette.middleware.base import BaseHTTPMiddleware


class TimerMiddleware(BaseHTTPMiddleware):

    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request, call_next):

        request.state.start_time = datetime.now()
        response = await call_next(request)
        process_time = datetime.now() - request.state.start_time
        response.headers["X-Process-Time"] = str(process_time.total_seconds())
        return response
