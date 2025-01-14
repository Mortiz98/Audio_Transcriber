# Audio Transcription API

## Description

This is an API built with **FastAPI** that transcribes audio files using OpenAI's **Whisper** model. It supports various audio formats and automatically converts files to MP3 when needed for transcription.

## Features
- **Accurate transcription** of audio files using the Whisper model.
- Automatic conversion of audio files to MP3 using `ffmpeg`.
- Validation of supported file formats.

## Prerequisites

Ensure you have the following installed:

- **Python 3.8 or later**
- **ffmpeg** (must be available in the command line)
- Required dependencies listed in `requirements.txt`:

```bash
fastapi
uvicorn
pydantic
whisper
```

Install them with:
```bash
pip install -r requirements.txt
```

## Installation

1. **Clone this repository**:
   ```bash
   git clone <REPOSITORY_URL>
   cd <REPOSITORY_NAME>
   ```

2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure ffmpeg is installed**. You can install it by following the instructions on [FFmpeg.org](https://ffmpeg.org/download.html).

## Usage

1. **Start the FastAPI server**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the interactive documentation**:
   - Open your browser and go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

3. **Available Endpoints**:

### GET /
- **Description**: Verifies the API's status.
- **Response**:
  ```json
  {
    "message": "Welcome to the Whisper Transcription API!"
  }
  ```

### POST /transcribe
- **Description**: Upload an audio file and receive the transcribed text.
- **Parameters**:
  - `file` (audio file, required): An audio file in MP3, WAV, OGG, OPUS, etc.
- **Successful Response**:
  ```json
  {
    "text": "Transcribed audio text."
  }
  ```
- **Status Codes**:
  - `200`: Successful transcription.
  - `400`: Unsupported file format.
  - `500`: Internal error processing the file.

## Example Request with cURL

```bash
curl -X POST "http://127.0.0.1:8000/transcribe" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@path_to_audio_file.mp3"
```

## Technologies Used
- **FastAPI**: Framework for building fast and efficient APIs.
- **Whisper**: OpenAI transcription model.
- **ffmpeg**: Tool for audio file conversion.

## Important Notes
- **File Sizes**: Ensure uploaded files are not excessively large to avoid performance issues.
- **Security**: Consider implementing authentication to secure access to this API.

## Contributions
If you'd like to contribute to this project, submit a pull request or open an issue to discuss the changes you'd like to make.


