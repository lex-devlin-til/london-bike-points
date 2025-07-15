import os
# import boto3
from dotenv import load_dotenv
load_dotenv()

aws_access = os.getenv('ACCESS_KEY')
aws_secret = os.getenv('SECRET_KEY')
bucket = os.getenv('S3_BUCKET')

print(aws_access, aws_secret, bucket)