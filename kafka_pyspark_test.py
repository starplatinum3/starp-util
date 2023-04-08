#encoding=utf8
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import kafka
import json
offsets = []
def out_put(m):
    print(m)
def store_offset(rdd):
    global offsets
    offsets = rdd.offsetRanges()
    return rdd
 
def print_offset(rdd):
    for o in offsets:
        print ("%s %s %s %s %s" % (o.topic, o.partition, o.fromOffset, o.untilOffset,o.untilOffset-o.fromOffset))
 
 
config = SparkConf()
scontext = SparkContext(appName='kafka_pyspark_test',)
stream_context = StreamingContext(scontext,2)
msg_stream = KafkaUtils.createDirectStream(stream_context,['asin_bsr_result',],kafkaParams={"metadata.broker.list": "3.120.9.44:9092,"})
result = msg_stream.map(lambda x :json.loads(x).keys()).reduce(out_put)
msg_stream.transform(store_offset,).foreachRDD(print_offset)

# Subscribe to 1 topic
# df = spark \
#   .readStream \
#   .format("kafka") \
#   .option("kafka.bootstrap.servers", "host1:port1,host2:port2") \
#   .option("subscribe", "topic1") \
#   .load()
# df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

result.pprint()
stream_context.start()
stream_context.awaitTermination()
 
# conda active 
#      from pyspark.streaming.kafka import KafkaUtils
# ModuleNotFoundError: No module named 'pyspark.streaming.kafka'
# conda activate py374
# [Anaconda] 使用conda activate激活环境出错_让我安静会的...
# 2022年8月26日 一个小细节,在输入source activate命令之前,一行的前面没有(base),输入source activate命令后,一行的前面显示有(base),此刻再conda activate env_name即可。 ...