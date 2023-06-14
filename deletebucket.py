import boto3

s3 = boto3.client('s3')
my_bucket = "my-bucket-boto321"
response = s3.delete_bucket(Bucket= my_bucket)
print("Bucket has been deleted successfully !!!")
