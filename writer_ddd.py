client = boto3.client('lambda', 'us-west-2')
resp = client.invoke(FunctionName='myfunction', InvocationType='RequestResponse', Payload="""{"rawValues": ["jero"], "replaceables": {"greeting": "world"}}""")