FROM python:3.10-slim
RUN apt-get update && apt-get install -y ffmpeg git build-essential && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . /app
RUN python -m pip install --upgrade pip
# Install CPU torch wheel (so it doesn't try to build GPU binaries)
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu
RUN pip install -r requirements.txt
EXPOSE 7860
CMD ["python","app.py"]
