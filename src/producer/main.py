import time
import json
from kafka import KafkaProducer
from src.producer.generate_data import get_weather
from src.utilities.enums import CONSTANTS, KAFKA_CONFIGURATION_CONSTANTS
from src.utilities.utilities import on_send_error, on_send_success


def kafka_producer():
    bootstrap = CONSTANTS.BOOTSTRAP_SERVER.value
    topic = CONSTANTS.KAFKA_TOPIC.value
    interval = CONSTANTS.INTERVAL.value

    producer = KafkaProducer(
        bootstrap_servers=[bootstrap],
        value_serializer=lambda x: json.dumps(x).encode(KAFKA_CONFIGURATION_CONSTANTS.ENCODING.value),
        retries=KAFKA_CONFIGURATION_CONSTANTS.RETRIES.value,
        linger_ms=KAFKA_CONFIGURATION_CONSTANTS.LINGER_MS.value,
        request_timeout_ms=KAFKA_CONFIGURATION_CONSTANTS.REQ_TIMEOUT_MS.value,
        max_block_ms=KAFKA_CONFIGURATION_CONSTANTS.MAX_BLOCK_MS.value,
    )
    while True:
        output = get_weather()
        print(output)
        future = producer.send(topic, value=output)
        future.add_callback(on_send_success)
        future.add_errback(on_send_error)
        time.sleep(interval)


if __name__ == "__main__":
    try:
        kafka_producer()
    except Exception as e:
        print(e)
