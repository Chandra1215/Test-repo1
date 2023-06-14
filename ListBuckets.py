import boto3
s3 = boto3.client('s3')
bucket_response =s3.list_buckets()
print('Existing buckets are:')
for bucket in bucket_response ['Buckets']:
    print(f'  {bucket["Name"]}')