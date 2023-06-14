import boto3
ec2=boto3.client('ec2')
responce=ec2.stop_instances( InstanceIds=[
        'i-06e627edf289167c1',
    ],
)
print(responce)