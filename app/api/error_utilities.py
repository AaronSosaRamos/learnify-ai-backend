from typing import Any
from pydantic import BaseModel

class ErrorResponse(BaseModel):
    """Base model for error responses."""
    status: int
    message: Any
    
    model_config = {
        "arbitrary_types_allowed": True
    }

class FileHandlerError(Exception):
    """Raised when a file content cannot be loaded. Used for tools which require file handling."""
    def __init__(self, message, url=None):
        self.message = message
        self.url = url
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"

class ImageHandlerError(Exception):
    """Raised when an image cannot be loaded. Used for tools which require image handling."""
    def __init__(self, message, url):
        self.message = message
        self.url = url
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"

class VideoTranscriptError(Exception):
    """Raised when a video transcript cannot be loaded. Used for tools which require video transcripts."""
    def __init__(self, message, url):
        self.message = message
        self.url = url
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"