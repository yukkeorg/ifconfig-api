import os
from fastapi import FastAPI, HTTPException

from .middlewares import cors
from .dependency import limit_params


app = FastAPI()
cors.set_middleware(app)


ALLOW_HTTP_ENVNAMES = [
    "HOST",
    "REMOTE_ADDR",
]


@app.get("/")
async def root():
    return {k: os.environ.get(k) for k in ALLOW_HTTP_ENVNAMES}


@app.get("/{env_names}")
async def root_envname(env_names: str):
    allowed_env_name_list = [en for en in env_names.split("+")
                             if en in ALLOW_HTTP_ENVNAMES]
    if allowed_env_name_list:
        return {e: os.environ.get(e) for e in allowed_env_name_list}
    else:
        raise HTTPException(status_code=404)