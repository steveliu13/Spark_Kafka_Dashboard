# coding: utf-8
import json
import random

from kafka import KafkaProducer
import csv
import time

from util.DataUtil import generateData

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def Producer():
    while True:
        data = generateData()
        producer.send("test", data.encode('utf-8'))
        time.sleep(1)
        print("数据传输成功")

