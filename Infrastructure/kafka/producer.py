from kafka import KafkaProducer
from kafka.errors import KafkaError
from django.conf import settings

import logging as log



def sendData(topic, data):
    producer = KafkaProducer(bootstrap_servers=str(settings.KAFKA_BOOTSTRAP_SERVERS))
    print(settings.KAFKA_BOOTSTRAP_SERVERS)
    future = producer.send(topic, data.encode('utf-8'))

    try:
        record_metadata = future.get(timeout=10)
    except KafkaError:
        log.exception()
        pass

    producer.flush()
    return record_metadata