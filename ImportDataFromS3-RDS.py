import boto3
import psycopg2

s3 = boto3.client('s3')
bucket_name = 'your-bucket-name'
file_name = 'your-file-name.csv'
local_file_path = 'local-file-path.csv'  # Path to save the downloaded file

s3.download_file(bucket_name, file_name, local_file_path)
