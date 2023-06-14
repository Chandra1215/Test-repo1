import pandas as pd

df = pd.read_csv('D:\PythonBoto3s3\Data.csv')
df.to_json('D:\PythonBoto3s3\my_file.json')