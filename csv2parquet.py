import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import boto3
import psycopg2

local_file_path = 'D:/Pythonboto3s3/annualsheet.csv'

df = pd.read_csv(local_file_path)

df.to_parquet('D:\PythonBoto3s3\DataSales.parquet')

# Connect to Amazon S3
s3 = boto3.client('s3')

# Define the S3 bucket and CSV file information
bucket_name = 'md5values-buck01'
file_name = 'DataSales.parquet'
local_file_parquet= 'D:\PythonBoto3s3\DataSales.parquet'



# Upload the file to S3
s3.upload_file(local_file_parquet, bucket_name, file_name)

# #connect to database 
# host = 'database-1.cpok0chvrmyk.ap-south-1.rds.amazonaws.com'
# port = 3306  
# database = 'TestDB'
# user = 'admin'
# password = 'Admin1122'

# conn = psycopg2.connect(host=host, port=port, database=database, user=user, password=password)
# cur = conn.cursor()

# table_name = 'AnnualSheetData'

# create_table_query = """
# CREATE TABLE IF NOT EXISTS {} (
#     Year INT,
#     Industry_aggregation_NZSIOC VARCHAR,
#     Industry_code_NZSIOC VARCHAR,
#     Industry_name_NZSIOC VARCHAR,
#     Units VARCHAR,
#     Variable_code VARCHAR,
#     Variable_name VARCHAR,
#     Variable_category VARCHAR,
#     Value VARCHAR,
#     Industry_code_ANZSIC06 VARCHAR
    
#     ...
# )
# """.format(table_name)

# cur.execute(create_table_query)

# import_query = """
# COPY {} FROM 's3://{}/{}'
# IAM_ROLE 'arn:aws:iam::365421589032:user/chandra'
# FORMAT AS PARQUET
# """.format(table_name, bucket_name, file_name)

# cur.execute(import_query)

# conn.commit()
# cur.close()
# conn.close()





