import boto3
import os
import sys
from urllib.parse import unquote_plus

s3_client = boto3.client('s3')
def handle_csv(original_csv_path, output_csv_path):
    # <process csv code>
    # process csv code
    print("process csv code")

# python - 如何在 AWS (EC2/Lambda) 上运行 python 代码 - IT工具网
# https://www.coder.work/article/7553364
def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])
        tmpkey = key.replace('/', '')
        # download_path = <insert path here>
        download_path = "<insert path here>"
        upload_path = "<insert path here>"
        # upload_path = <insert path here>
        s3_client.download_file(bucket, key, download_path)
        # s3_client_download_file
        handle_csv(download_path, upload_path)
        s3_client.upload_file(upload_path, '<>'.format(bucket), key)



import boto3
import json

lambda_client = boto3.client('lambda',
                             region_name='ap-northeast-2',
                             aws_access_key_id='XXXXXXXXXX',
                             aws_secret_access_key='XXXXXXXXXXX')
data = {"data1":"mydata"}

response = lambda_client.invoke(FunctionName="my_lambda_function",
                                InvocationType="Event",         ###for asynchronous purposes
                                Payload=json.dumps(data)
                                )

# 如何使用Python请求异步调用aws lambda函数 - 问答 - Python中文网
# https://www.cnpython.com/qa/1403486