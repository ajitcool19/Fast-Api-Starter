from datetime import datetime
import heapq

from fastapi import FastAPI
from starlette.requests import Request


class Middleware:
    def __init__(self, app : FastAPI, middlewares):

        middleware_priority = {
            "timer": 1,
            "proxy_mapper": 2,
            "auth": 3
        }

        priority_queue = [(middleware_priority[middleware], middleware) for middleware in middlewares]
        heapq.heapify(priority_queue)

        while priority_queue:
            _, middleware = heapq.heappop(priority_queue)

            if middleware == "timer":

               from common.middleware.middlewares.timer_middleware import TimerMiddleware
               app.add_middleware(TimerMiddleware)

            if middleware == "proxy_mapper":
                pass
            if middleware == "auth":

                from common.middleware.middlewares.auth_middleware import AuthMiddleware

                app.add_middleware(AuthMiddleware)




