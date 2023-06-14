import boto3
import json
s3 = boto3.client("s3")

    
response = s3.get_object(
Bucket='aws-web-hosting01',
Key='index.html')
print(response)