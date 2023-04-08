# from pyspark.sql.functions import *

import  pyspark.sql.functions  as F

from pyspark.sql import SparkSession

spark = SparkSession \
        .builder \
        .appName("StructuredNetworkWordCount") \
        .getOrCreate()

df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "test") \
    .load()

# df = df.rdd.map(lambda x: x.split(" ")).toDF()
df = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
df = df.withColumn("s", F.split(df['value'], " "))
df = df.withColumn('e', F.explode(df['s']))

q = df.writeStream \
    .format("console") \
    .trigger(processingTime='30 seconds')\
    .start()

q.awaitTermination()

# (1条消息) pyspark streaming与Kafka的应用及offset的手动设置_littlely_ll的博客-CSDN博客_pyspark kafka stream
# https://blog.csdn.net/littlely_ll/article/details/103933241

# 运行：
# spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.3 test.py

# spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.3  "D:\proj\python\my_util_py_pub\Structured Streaming.py"

# D:\env\spark-2.1.1-bin-hadoop2.4\bin\spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.3  "D:\proj\python\my_util_py_pub\Structured Streaming.py"

# 文档：# Denvspark-2.1.1-bin-hadoop2.4binsp...
# 链接：http://note.youdao.com/noteshare?id=f6f25a382cf7d82719a6714b5fe9b361&sub=B07A0017961F49C68CFD690CD05252AE