import boto3
s3 = boto3.client('s3')
my_bucket = "aws-cp-01"
file_name="Data.csv"
key_name ="Data.csv"
# response=s3.upload_file(Filename=file_name, Bucket=my_bucket, Key=key_name)
response = s3.put_object(Bucket=my_bucket,Key=key_name)
print(response)