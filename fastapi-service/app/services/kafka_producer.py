from confluent_kafka import Producer
import json
from app.config.kafka_config import KAFKA_CONFIG, TOPIC_NAME

# Initialize Kafka Producer
producer = Producer(KAFKA_CONFIG)

def send_to_kafka(key: str, value: dict):
    try:
        message = json.dumps(value, ensure_ascii=False)
        producer.produce(TOPIC_NAME, key=key, value=message.encode("utf-8"))
        producer.flush()
        return {"status": "success", "message": "Event sent to Kafka"}
    except Exception as e:
        return {"status": "error", "message": f"Failed to send event to Kafka: {str(e)}"}
    