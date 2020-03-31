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
        producer.send("test", generateData())

