
# import  spark 
from pyspark.sql.functions import *

# Subscribe to 1 topic
df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2") \
  .option("subscribe", "topic1") \
  .load()
df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Structured Streaming + Kafka Integration Guide (Kafka broker version 0.10.0 or higher) - Spark 3.3.1 Documentation
# https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html