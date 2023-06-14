import boto3

s3 = boto3.client('s3')
s3.create_bucket(Bucket='my-bucket9988', ACL='private',
CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
}
)