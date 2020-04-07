class BaseConfig(object):
    # 基础配置
    ZK_ADDRESS = 'localhost:9092'
    GENERATE_INTERVAL = 2
    PRODUCER_TOPIC = 'test'
    CONSUMER_TOPIC = 'test'
    SPARK_HOST = 'local[*]'
    SPARK_APP = 'DataProcessing'

class TestConfig(BaseConfig):
    # 测试环境配置
    AAA = 111

class DevConfig(BaseConfig):
    # 开发环境配置
    AAA = 222

class ProConfig(BaseConfig):
    # 线上环境配置
    AAA = 333