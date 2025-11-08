from pydantic import BaseModel

class InputModel(BaseModel):
    data_path: str
    model_path: str
    metrics_out: str
    plot_out: str

class OutputModel(BaseModel):
    message: str
    metrics_file: str
    plot_file: str
    mae: float
    r2: float