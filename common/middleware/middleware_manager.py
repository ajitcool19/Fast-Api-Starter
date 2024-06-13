import heapq

from fastapi import FastAPI


class Middleware:
    def __init__(self, app : FastAPI, middlewares):

        middleware_priority = {
            "db_session": 1,
            "timer": 2,
            "proxy_mapper": 2,
            "auth": 3
        }

        priority_queue = [(middleware_priority[middleware], middleware) for middleware in middlewares]
        heapq.heapify(priority_queue)

        while priority_queue:

            _, middleware = heapq.heappop(priority_queue)

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




