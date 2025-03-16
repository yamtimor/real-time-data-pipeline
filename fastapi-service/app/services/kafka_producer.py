from confluent_kafka import Producer
import json
from app.config.kafka_config import KAFKA_CONFIG, TOPIC_NAME

# Initialize Kafka Producer
producer = Producer(KAFKA_CONFIG)

