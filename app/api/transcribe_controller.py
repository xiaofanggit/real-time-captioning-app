from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from app.services.transcribe_service import transcribe_audio_file

router = APIRouter(tags=["Transcription"])

@router.post("/transcribe")
async def transcribe_audio(audio: UploadFile = File(...)):
    if not audio.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")

    try:
        result_text = await transcribe_audio_file(audio)
        return JSONResponse(content={"transcription": result_text})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
