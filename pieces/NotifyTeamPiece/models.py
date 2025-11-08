from pydantic import BaseModel
from typing import Optional

class InputModel(BaseModel):
    metrics_path: str
    webhook_url: Optional[str] = None

class OutputModel(BaseModel):
    message: str
    notification_sent: bool
    recipients: str