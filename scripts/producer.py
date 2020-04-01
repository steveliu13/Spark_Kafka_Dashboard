# coding: utf-8
from kafka import KafkaProducer
import time

from util.DataUtil import generateData

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def Producer():
    while True:
        data = generateData()
        producer.send("test", data.encode('utf-8'))
        time.sleep(2)
        print("kafka数据传输成功")

