from pyspark.sql import SQLContext, SparkSession

import pyspark

# python D:\proj\python\my_util_py_pub\pyspark_test.py


sparkContext=pyspark.SparkContext('local[*]')

spark=SparkSession.builder.appName("Spark SQL basic example").getOrCreate()