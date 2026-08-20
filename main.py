from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="Smart Sewing Pedal API",
    description="Backend for Smart Sewing Pedal Health Monitoring System",
    version="1.0.0"
)

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Store current pedal count
current_pedal_count = 0


# Data received from ESP32 later
class PedalData(BaseModel):
    pedal_count: int


@app.get("/")
def home():
    return {
        "message": "Smart Sewing Pedal Backend is running!",
        "status": "connected"
    }


# Dashboard gets the current count
@app.get("/pedal-count")
def get_pedal_count():
    return {
        "pedal_count": current_pedal_count
    }


# ESP32 will use this later
@app.post("/pedal-count")
def update_pedal_count(data: PedalData):
    global current_pedal_count

    current_pedal_count = data.pedal_count

    return {
        "message": "Pedal count received successfully",
        "pedal_count": current_pedal_count
    }