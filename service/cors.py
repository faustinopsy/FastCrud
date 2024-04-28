from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:966",
    "http://localhost:8000",
    "http://127.0.0.1:5500",
]

def add_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    