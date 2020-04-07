## 实时交易数据分析平台
### 序章
+ 公司的带数据培训实战营要做出一个东西来，作为新组长试试做一个朴素的demo；
+ 本来想用springboot做的，框架都搭好了，卡在了socketio上，正好看到有个flask+socketio+echarts的CPU监控工具（不知道哪个博客是真的原创，就放这个[链接](https://www.cnblogs.com/hhh5460/p/7397006.html)）比较值得借鉴，就改成了相同的框架；
+ 改成python后卡最长时间的json的序列化和反序列化，最后参考了（同样不知道是不是原的）[链接](https://www.cnblogs.com/magic8sky/p/10475704.html)，在此基础上写了一个反序列化为对象List的方法；
+ spark-streaming-kafka如果报错 Spark Streaming's Kafka libraries not found in class path. Try one of the following. 参考[链接](https://blog.csdn.net/weixin_40161254/article/details/103296937) 解决；

### 准备工作
1. 会python，flask，基本的前端语法
2. 部署一个单机的kafka，mac可以参考[链接](https://www.jianshu.com/p/23b75520a632)
3. 我的环境是python3.7(anaconda版)+pyCharm，需要第三方库包括Flask，Flask-SocketIO，Kafka和尚未用到的pyspark
4. 最后测试的浏览器用chrome或safari，360极速浏览器可能会吃掉CSS

### 工作流程
1. 定时生成若干条随机数据，转为Json
2. Producer传输这些数据
3. Consumer接收这些数据
4. 数据反序列化后传给SparkStreaming处理
5. 将处理好的数据传输给socket-io
6. 前端通过echarts绘制实时折线图

### 展示页面
1. 总体展示
2. 4个城市对比
3. 男女对比
4. 4种支付方式对比
5. 6种消费类型对比

### 后续工作
- [ ] 数据处理改为spark流计算
- [ ] 写个博客介绍一下
- [x] 加个配置文件，把kafka，spark这些配置放里面
- [ ] 可能会学习一下前端，把页面做好看一点

