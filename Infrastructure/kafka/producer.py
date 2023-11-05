from kafka import KafkaProducer
from kafka.errors import KafkaError
from django.conf import settings

import logging as log

producer = KafkaProducer(bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS)

def sendData(topic, data):
   
    future = producer.send(topic, data.encode('utf-8'))
 

    try:
        record_metadata = future.get(timeout=10)
    except KafkaError:
        log.exception( "KafkaError: " + str(KafkaError) )
        pass

    producer.flush()
    return record_metadata