from buisness_logic.routes.buisness_logic_routes import router as buisness_logic_router
from user_management.routes.user_routes import router as user_router

class Routes:
    def __init__(self, app):
        self.app = app

    def include_routes(self):
        self.app.include_router(buisness_logic_router)
        self.app.include_router(user_router)

