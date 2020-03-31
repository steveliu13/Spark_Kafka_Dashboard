from kafka import KafkaConsumer

def Consumer():
    consumer = KafkaConsumer('test',bootstrap_servers='localhost:9092')
    return consumer


