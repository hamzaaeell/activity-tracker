import boto3
import os
from botocore.exceptions import ClientError

class AWSClient:
    def __init__(self):
        self.s3 = boto3.client(
            's3',
            region_name=os.getenv('AWS_REGION', 'us-east-1'),
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
            aws_secret_access_key=os.getenv('AWS_SECRET_KEY')
        )
        self.bucket = os.getenv('AWS_BUCKET', 'your-aws-bucket')

    def upload_file(self, file_path: str, s3_key: str):
        try:
            self.s3.upload_file(file_path, self.bucket, s3_key)
            print(f"Uploaded {file_path} to S3")
        except ClientError as e:
            print(f"AWS Error: {e}")
