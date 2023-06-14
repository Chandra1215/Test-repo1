import boto3
s3=boto3.client('s3')
bucket="aws-cp-01"
key="hello1.txt"
Object_list=s3.list_objects(Bucket=bucket)
for objects in Object_list["Contents"]:
    print(objects['Key'])
    if objects ==key:
        s3.delete_object(
            Bucket=bucket,
            Key=key)
        print("Object Deleted Successfully")
    else:
        print("No Such Objects Found in the Bucket")
    