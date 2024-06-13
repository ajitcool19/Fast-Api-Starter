import os

from contextvars import ContextVar

env = ContextVar('env', default=None)


def get_env():
    return env.get() or os.environ.get('env')