from fastapi.middleware.cors import CORSMiddleware


base_origins = [
    "http://localhost",
    "http://localhost:8000",
]

def set_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=base_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )