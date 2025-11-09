from pydantic import BaseModel

class InputModel(BaseModel):
    model_path: str
    features_csv: str
    output_csv: str
    output_plot: str

class OutputModel(BaseModel):
    message: str
    forecast_file: str
    plot_file: str