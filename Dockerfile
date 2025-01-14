# 1. Using a Python 3.10 base image
FROM python:3.10

# 2. Install ffmpeg (necessary to process audios with Whisper)
RUN apt-get update && apt-get install -y ffmpeg

# 3. Set the working directory inside the container
WORKDIR /app

# 4. Copy the requirements.txt file to the container
COPY requirements.txt requirements.txt

# 5. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy all source code to the container
COPY . .

# 7. Command to run the application when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
