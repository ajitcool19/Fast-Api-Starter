from fastapi import FastAPI
from common.middleware.middleware_manager import Middleware
from common.routes import Routes
from common.monitoring.sentry import init_sentry

init_sentry() # Comment this line if you don't want to use sentry


app = FastAPI()
Middleware(app, ["login","db_session","timer","auth"])


Routes(app).include_routes()
