import boto3
s3 = boto3.client('s3')
my_bucket = "static-webapp-01"
key_name = "4.jpg"
response=s3.delete_object(Bucket=my_bucket, Key=key_name)
print(response)