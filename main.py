import os
import boto3
from dotenv import load_dotenv

# Load the AWS credentials from the .env file
load_dotenv()

# Create a session using the loaded AWS credentials
session = boto3.Session(
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION')
)

# Create an S3 client
s3 = session.client('s3')

# List all the objects in the bucket
response = s3.list_objects_v2(Bucket='toolbox-storage')
for obj in response['Contents']:
    print(obj['Key'])

""" # Upload a file to the bucket
s3.upload_file('LOCAL_FILE_PATH', 'YOUR_BUCKET_NAME', 'OBJECT_KEY')

# Download a file from the bucket
s3.download_file('YOUR_BUCKET_NAME', 'OBJECT_KEY', 'LOCAL_FILE_PATH') """
