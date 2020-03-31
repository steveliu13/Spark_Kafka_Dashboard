from kafka import KafkaConsumer

def Consumer():
    consumer = KafkaConsumer('test',bootstrap_servers='localhost:9092')
    # for msg in consumer:
    #     print((msg.value).decode('utf8'))
    return consumer


