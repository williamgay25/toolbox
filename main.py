import os
import time
import boto3
import qrcode
import logging
from io import BytesIO
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

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

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Load the AWS credentials from the .env file
AWS_REGION = os.getenv('AWS_REGION')
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

# Create a session using the loaded AWS credentials
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

# Create an S3 client
s3 = session.client('s3')

@app.get('/')
async def root():
    return HTMLResponse(content='<h1>QR Code Generator</h1>')

@app.get('/ping')
async def ping():
    return {'message': 'pong'}

@app.post('/generate_qr_code')
async def generate_qr_code(website_link: str):
    try:
        # log the request
        logger.info(f'Generating QR code for {website_link}')

        # Generate QR code image
        qr = qrcode.QRCode()
        qr.add_data(website_link)
        qr.make()

        # Create an image file from the QR code
        qr_image = qr.make_image()

        # Generate a unique filename using a timestamp
        timestamp = int(time.time())  # Get current timestamp
        qr_image_path = f'qr_code_{timestamp}.png'  # Unique filename

        # Save the QR code image to a BytesIO object
        qr_image_bytes = BytesIO()
        qr_image.save(qr_image_bytes, format='PNG')
        qr_image_bytes.seek(0)

        # Upload the image file to the S3 bucket
        s3.upload_fileobj(qr_image_bytes, S3_BUCKET_NAME, qr_image_path)

        # Construct the URL of the uploaded QR code image
        qr_image_url = f'https://{S3_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{qr_image_path}'

        # Return the URL of the QR code image
        return {'qr_code_url': qr_image_url}
    except Exception as e:
        logger.error(f"Error in generate_qr_code: {e}")
        raise