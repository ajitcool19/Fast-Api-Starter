import time
from fastapi import FastAPI
from common.middleware.middleware_manager import Middleware
from common.routes import Routes
app = FastAPI()
Middleware(app, ["timer","auth"])
Routes(app).include_routes()

