import os
from fastapi import FastAPI

app = FastAPI()

allow_http_envnames = [
    "REMOTE_ADDR",
]


@app.get("/")
def read_root():
    return {k: os.environ.get(k, "") for k in allow_http_envnames}
