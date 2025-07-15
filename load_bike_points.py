import os
import boto3
from dotenv import load_dotenv
load_dotenv()

aws_access = os.getenv('ACCESS_KEY')
aws_secret = os.getenv('SECRET_KEY')
bucket = os.getenv('S3_BUCKET')

print(aws_access, aws_secret, bucket)

s3_client = boto3.client(
            's3',
            aws_access_key_id = aws_access,
            aws_secret_access_key = aws_secret
)

print(s3_client)

filename = 'data/2025-07-09_16-27-53.json'
s3filename = 'bike-points/2025-07-09_16-27-53.json'
try:
    s3_client.upload_file(filename, bucket, s3filename)
    print(f'{filename} uploaded successfully.')
except:
    print('something went wrong uploading the file')