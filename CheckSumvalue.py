import hashlib
import boto3
s3 = boto3.client('s3')

bucket = 'checksumvaluesfiles012'
key='AwsSheet.XLSX'
def s3_upload(bucket,key):
    with open(key, 'rb') as file:
        response = s3.put_object(Bucket=bucket, Key=key,ChecksumAlgorithm="sha256")                                 
        result = s3.get_object(Bucket=bucket,Key=key,ChecksumMode="ENABLED")
        print(result['ChecksumSHA256'])
s3_upload(bucket,key)