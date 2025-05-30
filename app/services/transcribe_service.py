import tempfile
import whisper
from fastapi import UploadFile

# Load the model once at service level
model = whisper.load_model("base")

async def transcribe_audio_file(audio_file: UploadFile) -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        contents = await audio_file.read()
        temp_audio.write(contents)
        temp_audio.flush()
        result = model.transcribe(temp_audio.name)
        return result["text"]
