from fastapi import FastAPI
import socket
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "status": "healthy",
        "message": "DevOps Microservice is running locally!",
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENV", "development")
    }

@app.get("/health")
def health_check():
    return {"status": "UP"}
