from kafka import KafkaConsumer

#kafka消费者
def Consumer():
    # kafka的topic用test，部署在本机
    # 暂时不用配置文件的方式
    consumer = KafkaConsumer('test',bootstrap_servers='localhost:9092')
    return consumer


