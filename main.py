from fastapi import FastAPI
from datetime import datetime, date

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


@app.get("/date")
def get_date():
    today = date.today()
    return {
        "server_date": today.strftime("%Y-%m-%d"),
        "iso": today.isoformat(),
        "day_of_week": today.strftime("%A"),
    }
