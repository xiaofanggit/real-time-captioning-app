from pydantic import BaseModel


class TranscriptResponse(BaseModel):
    transcription: str
