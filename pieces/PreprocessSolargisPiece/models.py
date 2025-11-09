from pydantic import BaseModel

class InputModel(BaseModel):
    input_path: str
    output_path: str

class OutputModel(BaseModel):
    message: str
    processed_rows: int
    output_file: str