from uuid import uuid4

from starlette.middleware.base import BaseHTTPMiddleware
from common.configs.logging.logging_config import logger


class RouterLoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app) -> None:
        self._logger = logger
        super().__init__(app)

    async def dispatch(self, request, call_next):
        request_id: str = str(uuid4())
        logging_dict = {
            "X-API-REQUEST-ID": request_id
        }
        request.state.request_id = request_id
        self._logger.info("Request received", extra=logging_dict)

        response = await call_next(request)

        self._logger.info("Request completed", extra=logging_dict)
        return response


