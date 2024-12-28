from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import whisper
from io import BytesIO

app = FastAPI()

# Cargar el modelo Whisper
model = whisper.load_model("base")  # Puedes usar otros modelos como "small", "medium", "large"

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    # Leer el archivo de audio
    audio_data = await file.read()
    audio = BytesIO(audio_data)

    # Transcribir el audio usando Whisper
    result = model.transcribe(audio)

    # Devolver la transcripción
    return {"transcription": result["text"]}
