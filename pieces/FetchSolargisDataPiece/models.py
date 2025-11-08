from pydantic import BaseModel
from typing import Optional

class InputModel(BaseModel):
    s3_path: str
    output_path: str

class OutputModel(BaseModel):
    message: str
    downloaded_file: str