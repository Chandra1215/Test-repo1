import boto3

ec2 = boto3.client('ec2')
response = ec2.start_instances(
    InstanceIds=[
        'i-06e627edf289167c1',
    ],
)

print(response)