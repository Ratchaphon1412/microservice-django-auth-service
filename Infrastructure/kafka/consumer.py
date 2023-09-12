from kafka import KafkaConsumer
from kafka.errors import KafkaError
from django.conf import settings
from ..event.listener.topic import Listener
import json
import sys 
import threading



class Consumer(threading.Thread):
    def __init__(self,topic,group):
        threading.Thread.__init__(self)
        self.topic = topic # array of topics
        self.group = group
        self.consumer = KafkaConsumer(bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,auto_offset_reset='earliest',enable_auto_commit=True,group_id=group)
        


    def run(self):
        # Override the run method of the thread class
        self.consumer.subscribe(self.topic)
        try:
            for message in self.consumer:
            # message value and key are raw bytes -- decode if necessary!
            # e.g., for unicode: `message.value.decode('utf-8')`
                # print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                #                                     message.offset, message.key,
                #                                     message.value))
                
                Listener.run(message.topic,message.value)
               
                
        except KafkaError as e:
            print(e)
        finally:
            self.consumer.close()
            return None

