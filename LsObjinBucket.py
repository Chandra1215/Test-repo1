import boto3
s3=boto3.client('s3')
Object_list=s3.list_objects(Bucket="aws-cp-01")
for objets in Object_list["Contents"]:
    print(objets["Key"])