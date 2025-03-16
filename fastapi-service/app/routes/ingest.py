from fastapi import APIRouter
from pydantic import BaseModel
from app.services.kafka_producer import send_to_kafka

router = APIRouter()

# Define request body
class Event(BaseModel):
    key: str
    value: str

@router.post("/ingest")
def ingest_data(event: Event):
    return send_to_kafka(event.key, event.value)
