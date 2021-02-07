import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

base_origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=base_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


allow_http_envnames = [
    "HOST",
    "REMOTE_ADDR",
]


@app.get("/")
async def root():
    return {k: os.environ.get(k) for k in allow_http_envnames}


@app.get("/{env_names}")
async def root_envname(env_names: str):
    allowed_env_name_list = [en for en in env_names.split("+")
                             if en in allow_http_envnames]
    if allowed_env_name_list:
        return {e: os.environ.get(e) for e in allowed_env_name_list}
    else:
        raise HTTPException(status_code=404, detail="Not Found")


