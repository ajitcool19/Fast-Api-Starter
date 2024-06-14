import heapq

from fastapi import FastAPI
from common.configs.config import current_config

class Middleware:
    def __init__(self, app : FastAPI, middlewares):

        middleware_priority = {
            "db_session": 1,
            "login": 2,
            "timer": 2,
            "proxy_mapper": 2,
            "auth": 3
        }

        priority_queue = [(middleware_priority[middleware], middleware) for middleware in middlewares]
        heapq.heapify(priority_queue)

        while priority_queue:

            _, middleware = heapq.heappop(priority_queue)

            if middleware == "login":
                from common.middleware.middlewares.login_middleware import LoginMiddleware
                app.add_middleware(LoginMiddleware)

            if middleware == "db_session":
                from common.middleware.middlewares.db_session_middleware import DbSessionMiddleware
                app.add_middleware(DbSessionMiddleware)

            if middleware == "timer":

               from common.middleware.middlewares.timer_middleware import TimerMiddleware
               app.add_middleware(TimerMiddleware)

            if middleware == "proxy_mapper":
                pass
            if middleware == "auth":

                from common.middleware.middlewares.auth_middleware import AuthMiddleware

                app.add_middleware(AuthMiddleware)




