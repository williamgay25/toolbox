import os
import time
from fastapi import FastAPI
import boto3
import qrcode
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load the AWS credentials from the .env file
load_dotenv()

# Create a FastAPI instance
app = FastAPI()

# Allow requests from the frontend
origins = ["*"]

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

REGION_NAME = os.getenv('AWS_REGION_NAME')
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

# Create a session using the loaded AWS credentials
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION_NAME
)

# Create an S3 client
s3 = session.client('s3')

# List all the objects in the bucket
response = s3.list_objects_v2(Bucket=S3_BUCKET_NAME)
for obj in response['Contents']:
    print(obj['Key'])

@app.post('/generate_qr_code')
async def generate_qr_code(website_link: str):
    # Generate QR code image
    qr = qrcode.QRCode()
    qr.add_data(website_link)
    qr.make()

    # Create an image file from the QR code
    qr_image = qr.make_image()

    # Generate a unique filename using a timestamp
    timestamp = int(time.time())  # Get current timestamp
    qr_image_path = f'qr_code_{timestamp}.png'  # Unique filename

    # Save the QR code image to a file
    qr_image.save(qr_image_path)

    # Upload the image file to the S3 bucket
    s3.upload_file(qr_image_path, S3_BUCKET_NAME, qr_image_path)

    # Remove the local image file
    # (comment out if you want to keep a local copy)
    os.remove(qr_image_path)

    # Construct the URL of the uploaded QR code image
    qr_image_url = f'https://{S3_BUCKET_NAME}.s3.{REGION_NAME}.amazonaws.com/{qr_image_path}'

    # Return the URL of the QR code image
    return {'qr_code_url': qr_image_url}