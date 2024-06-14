import logging.config
import logging
import os
import sys
from datetime import datetime
from multiprocessing import Queue

from logging_loki import LokiQueueHandler

from common.configs.config import current_config


path = current_config.BASE_PATH + "/logs" + "/" + datetime.now().strftime("%Y-%m-%d") + ".log"
print(path)
if  not os.path.exists(current_config.BASE_PATH + "/logs"):
    os.mkdir(current_config.BASE_PATH + "/logs")

logging_config = {
    "version": 1,
    "formatters": {
        "json": {
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(process)s %(levelname)s %(funcName)s %(lineno)s %(message)s %(X-API-REQUEST-ID)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "json",
            "stream": sys.stderr,
        },
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "formatter": "json",
            "filename": path,
            "mode": "a",  # Append mode
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "console",
            "file"
        ],
        "propagate": True
    }
}

# loki_logs_handler = LokiQueueHandler(
#     Queue(-1),
#     url=current_config.LOKI_URL,
#     tags={"application": "fastapi"},
#     version="1",
# )

logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__)
# logger.addHandler(loki_logs_handler) add in case you want to send logs to loki
