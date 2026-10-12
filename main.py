from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="Time Server")


@app.get("/")
def root():
    return {"message": "Welcome to the Time Server!"}


@app.get("/time")
def get_time():
    now = datetime.now()
    return {
        "server_time": now.strftime("%Y-%m-%d %H:%M:%S"),
        "iso": now.isoformat(),
        "timezone": "local",
    }
