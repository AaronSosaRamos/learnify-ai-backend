from pydantic import BaseModel, Field
from typing import Literal, List

class AIResistantArgs(BaseModel):
    topic: str = Field(..., min_length=1, max_length=255, description="Topic or subject related to the content")
    assignment: str = Field(..., min_length=1, max_length=255, description="The given assignment")
    grade_level: Literal["elementary", "middle", "high", "college", "professional"] = Field(..., description="Educational level to which the content is directed")
    file_type: str = Field(..., description="Type of file being handled, according to the defined enumeration")
    file_url: str = Field(..., description="URL or path of the file to be processed")
    lang: str = Field(..., description="Language in which the file or content is written")

class AIResistanceIdea(BaseModel):
    assignment_description: str = Field(..., description="Detailed description of the modified assignment")
    explanation: str = Field(..., description="Explanation of how this modification makes the assignment AI-resistant")

class AIResistantOutput(BaseModel):
    topic: str = Field(..., description="Topic or subject related to the assignment")
    grade_level: str = Field(..., description="Educational level to which the assignment is directed")
    ideas: List[AIResistanceIdea] = Field(..., description="List of 3 ideas to make the assignment AI-resistant, including explanation")