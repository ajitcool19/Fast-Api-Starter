from fastapi import APIRouter

from buisness_logic.buisness_logic_routes import router as buisness_logic_router


class Routes:
    def __init__(self, app):
        self.app = app

    def include_routes(self):
        self.app.include_router(buisness_logic_router)

