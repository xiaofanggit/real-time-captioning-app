from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.api.transcribe_controller import router as transcribe_router

app = FastAPI(title="Whisper Transcription Service")

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(transcribe_router, prefix="/api")
