from fastapi import FastAPI
from common.middleware.middleware_manager import Middleware
from common.routes import Routes
from common.monitoring.sentry import init_sentry
from common.configs.config import current_config
import os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.mkdir("logs") if not os.path.exists("logs") else None
os.mkdir("sqllite_db") if not os.path.exists("sqllite_db") else None

# init_sentry() # Comment this line if you don't want to use sentry


app = FastAPI()
Middleware(app, current_config.MIDDLEWARES)


Routes(app).include_routes()
