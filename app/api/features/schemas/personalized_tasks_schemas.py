from pydantic import BaseModel, Field
from typing import List

class ConnectWithThemArgs(BaseModel):
    grade_level: str = Field(..., description="The grade level the teacher is instructing.")
    task_description: str = Field(..., description="A brief description of the subject or topic the teacher is instructing.")
    students_description: str = Field(..., description="A description of the students including age group, interests, location, and any relevant cultural or social factors.")
    file_url: str = Field(..., description="URL of any relevant file associated with the teaching material.")
    file_type: str = Field(..., description="The type of the file")
    lang: str = Field(..., description="The language in which the subject is being taught.")

class Recommendation(BaseModel):
    project_overview: str = Field(..., description="A detailed description of the project or activity recommendation.")
    rationale: str = Field(..., description="An explanation of why this recommendation is relevant to the students' interests or background.")
    difficulty_level: str = Field(..., description="The difficulty level of the project (e.g., easy, moderate, challenging).")
    required_tools: List[str] = Field(..., description="A list of tools, software, or resources required to complete the project.")
    estimated_time: str = Field(..., description="The estimated time to complete the project or activity.")

class RecommendationsOutput(BaseModel):
    recommendations: List[Recommendation] = Field(..., description="A list of personalized recommendations based on the input.")