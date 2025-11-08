import boto3
import os
from urllib.parse import urlparse
from models import InputModel, OutputModel

def main(input_model: InputModel) -> OutputModel:
    print(f"[INFO] Fetching data from {input_model.s3_path} → {input_model.output_path}")
    
    # Parse S3 path
    parsed = urlparse(input_model.s3_path, allow_fragments=False)
    if parsed.scheme == "s3":
        bucket = parsed.netloc
        key = parsed.path.lstrip('/')
        
        # Initialize S3 client
        s3 = boto3.client('s3')
        
        # Create output directory if not exists
        os.makedirs(os.path.dirname(input_model.output_path), exist_ok=True)
        
        # Download file
        s3.download_file(bucket, key, input_model.output_path)
        print(f"[SUCCESS] Downloaded {input_model.s3_path}")
        
        return OutputModel(
            message=f"Successfully downloaded {input_model.s3_path}",
            downloaded_file=input_model.output_path
        )
    else:
        raise ValueError("Only S3 paths are supported")

if __name__ == "__main__":
    # For testing purposes
    input_data = InputModel(
        s3_path="s3://bucket/data.csv",
        output_path="/mnt/artifacts/data.csv"
    )
    result = main(input_data)
    print(result)