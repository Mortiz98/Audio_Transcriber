from fastapi import FastAPI, File, UploadFile, HTTPException 
from pydantic import BaseModel
import whisper
from tempfile import NamedTemporaryFile
import os
import subprocess 


# Inicializar la aplicación FastAPI
app = FastAPI(title="Audio Transcription API", description="API para transcribir audios usando Whisper")

# Cargar el modelo de Whisper
model = whisper.load_model("base")

class TranscriptionResult(BaseModel):
    text: str
# Función para convertir el archivo de audio a mp3 usando ffmpeg
def convert_to_mp3(input_file_path: str) -> str:
    # Crear un archivo temporal .mp3
    output_file_path = input_file_path.rsplit(".", 1)[0] + ".mp3"
    
    # Ejecutar el comando ffmpeg para convertir el archivo
    subprocess.run(["ffmpeg", "-i", input_file_path, output_file_path], check=True)
    
    return output_file_path

@app.post("/transcribe", response_model=TranscriptionResult)
async def transcribe_audio(file: UploadFile = File(...)):
    """
    Endpoint para transcribir un archivo de audio.
    
    Args:
        file (UploadFile): Archivo de audio subido por el usuario.

    Returns:
        TranscriptionResult: Texto transcrito del audio.
    """
    if file.content_type not in ["audio/mpeg", "audio/wav", "audio/x-wav", "audio/mp3","audio/opus"]:
        raise HTTPException(status_code=400, detail="Formato de archivo no soportado.")

    try:
        # Guardar el archivo temporalmente
        file_extension = file.filename.split('.')[-1]
        suffix = f".{file_extension}" if file_extension else ".mp3"
        
        with NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
            temp_file.write(await file.read())
            temp_file_path = temp_file.name
            
        if file_extension != "mp3":
            temp_file_path = convert_to_mp3(temp_file_path)
            

        # Realizar la transcripción
        result = model.transcribe(temp_file_path)
        
        # Eliminar el archivo temporal
        os.remove(temp_file_path)

        return TranscriptionResult(text=result["text"])

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar el archivo: {str(e)}")

# Mensaje de bienvenida
@app.get("/")
def read_root():
    """
    Endpoint raíz para verificar el estado de la API.
    """
    return {"message": "Bienvenido a la API de Transcripción con Whisper!"}


