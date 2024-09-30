from typing import Any
from pydantic import BaseModel

class ErrorResponse(BaseModel):
    """Base model for error responses."""
    status: int
    message: Any
    
    model_config = {
        "arbitrary_types_allowed": True
    }