from pydantic import BaseModel
from typing import Optional

class InputModel(BaseModel):
    model_path: str
    metrics_path: str
    name: str
    description: Optional[str] = ""

class OutputModel(BaseModel):
    message: str
    model_version_id: str
    registry_url: str