import pandas as pd
import boto3

s3 = boto3.client('s3')
src ="s3://mycsvfiles02/test.csv"
x = pd.read_csv(src)
print(x)