import { useState } from "react";
import { useRecorder } from "./components/useRecorder";

function App() {
  const { recording, blob, startRecording, stopRecording } = useRecorder();
  const [transcription, setTranscription] = useState("");

  const sendAudio = async () => {
    if (!blob) return;

    const formData = new FormData();
    formData.append("audio", blob, "recording.wav");

    const response = await fetch("http://localhost:5000/api/transcribe", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    setTranscription(data.transcription || "Error transcribing.");
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>🎙️ Real-Time Captioning</h1>
      <div>
        <button onClick={startRecording} disabled={recording}>
          Start
        </button>
        <button onClick={stopRecording} disabled={!recording}>
          Stop
        </button>
        <button onClick={sendAudio} disabled={!blob}>
          Transcribe
        </button>
      </div>

      <h2>📝 Transcription:</h2>
      <p>{transcription}</p>
    </div>
  );
}

export default App;
