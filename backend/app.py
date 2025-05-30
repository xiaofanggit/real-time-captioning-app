from flask import Flask, request, jsonify
from flask_cors import CORS
import tempfile
import whisper

app = Flask(__name__)
CORS(app)

model = whisper.load_model("base")

@app.route("/api/transcribe", methods=["POST"])
def transcribe_audio():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file uploaded."}), 400

    audio_file = request.files["audio"]
    if audio_file.filename == "":
        return jsonify({"error": "Empty filename."}), 400

    # Save to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        audio_file.save(temp_audio.name)
        result = model.transcribe(temp_audio.name)
        return jsonify({"transcription": result["text"]})
    
if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
