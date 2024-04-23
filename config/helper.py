from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:966",
    "http://localhost:8000",
]

def add_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
