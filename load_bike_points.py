import os
import boto3
from dotenv import load_dotenv

def load_bike_points():
    load_dotenv()

    aws_access = os.getenv('ACCESS_KEY')
    aws_secret = os.getenv('SECRET_KEY')
    bucket = os.getenv('S3_BUCKET')

    s3_client = boto3.client(
                's3',
                aws_access_key_id = aws_access,
                aws_secret_access_key = aws_secret
    )

    print('Load script initializing...')
    # Find the first file in the data folder. There should only ever be one at a time.
    try:
        for file in os.listdir('data'):
            if file[-5:] == '.json':
                filename = file
                print(f'Found file: {filename} in data folder.')
    except:
        print('There was an error finding the file.')

    # Define filepaths for local machine and for S3 upload
    localfile = 'data/' + filename
    s3file = 'bike-points/' + filename

    # Upload the file to S3 then delete
    try:
        s3_client.upload_file(localfile, bucket, s3file)
            # see if we're overwriting - give a message if the filenames are the same
        print(f'{filename} uploaded to S3 bucket {bucket} successfully.')
        try:
            os.remove(localfile)
            print(f'{filename} deleted from local machine.')
        except:
            print('File not deleted from local machine')
    except:
        print('Something went wrong uploading the file')

if __name__ == '__main__':
    load_bike_points()