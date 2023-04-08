from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# local 必须设为2
sc = SparkContext("local[2]", "NetworkWordCount")
ssc = StreamingContext(sc, 1)

lines = ssc.socketTextStream("localhost", 9999)

words = lines.flatMap(lambda line: line.split(" "))

pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)

wordCounts.pprint()

ssc.start()
ssc.awaitTermination()


# pyspark streaming简介 和 消费 kafka示例_Crazy灬峰少的博客-CSDN博客_pyspark streaming kafka
# https://blog.csdn.net/qq_22918243/article/details/89336645
