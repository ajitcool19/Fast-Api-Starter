import sys

import uvicorn

from common.environment import env, get_env

environment = sys.argv[1]

if environment not in ['local', 'dev', 'prod']:
    raise ValueError('Unsupported env')


env.set(environment)

if __name__ == "__main__":
    uvicorn.run("startup.main:app", host="0.0.0.0", port=8000, reload=False)
    # if get_env() in ['local', 'dev','prod']:
    #     uvicorn.run("startup.main:app", host="0.0.0.0", port=8000, reload=False)
    # else:
    #     uvicorn.run("startup.main:app", host="0.0.0.0", port=8000, reload=True)
