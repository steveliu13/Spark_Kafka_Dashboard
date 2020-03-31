import json
import time
from threading import Lock

from concurrent.futures import ThreadPoolExecutor

import psutil as psutil
from flask import Flask, render_template
from flask_socketio import SocketIO
from kafka import KafkaConsumer

from scripts.consumer import Consumer
from scripts.producer import Producer
from util import JsonUtil
from util.DataUtil import consumeRecord
from util.JsonUtil import json_deserialize2objlist

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,async_mode=None)
thread = None

executor = ThreadPoolExecutor(1)
thread_lock = Lock()

# 后台线程 产生数据，即刻推送至前端
def background_thread():
    executor.submit(some_long_task1)
    count = 0
    for msg in Consumer():
        json_data = msg.value.decode('utf-8')
        print(json_data)
        result = json_deserialize2objlist(json_data, consumeRecord)
        scores = []
        for res in result:
            scores.append(res.amount)

        count += 1
        t = time.strftime('%M:%S', time.localtime()) # 获取系统时间（只取分:秒）
        # cpus = psutil.cpu_percent(interval=None, percpu=True) # 获取系统cpu使用率 non-blocking
        # print(cpus)
        socketio.emit('server_response',
                      # {'data': [t, *cpus], 'count': count},
                      {'data': [t, *scores], 'count': count},
                      namespace='/test') # 注意：这里不需要客户端连接的上下文，默认 broadcast = True ！！！！！！！
        socketio.sleep(1)


def some_long_task1():
    Producer()

# 与前端建立 socket 连接后，启动后台线程
@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)



@app.route("/")
def handle_mes():
    return render_template("test.html",async_mode=socketio.async_mode)


if __name__ == '__main__':
    socketio.run(app,debug=True)