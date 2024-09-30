from pydantic import BaseModel, Field
from typing import Literal, List, Any

class RubricGeneratorArgs(BaseModel):
    grade_level: Literal["elementary", "middle", "high", "college", "professional"] = Field(..., description="Educational level to which the content is directed")
    point_scale: str = Field(..., description="Point scale used for the assignment (e.g., 100-point scale, 4.0 GPA scale)")
    standard: str = Field(..., description="Educational standard or guideline being followed")
    file_type: str = Field(..., description="Type of file being handled, according to the defined enumeration")
    file_url: str = Field(..., description="URL or path of the file to be processed")
    lang: str = Field(..., description="Language in which the file or content is written")

class ScoreRange(BaseModel):
    label: str = Field(..., description="Label for the score range (e.g., 'Excellent', 'Good')")
    min_score: int = Field(..., description="Minimum score for this label")
    max_score: int = Field(..., description="Maximum score for this label")
    description: str = Field(..., description="Description for this score range")

class RubricCriterion(BaseModel):
    criterion_name: str = Field(..., description="Name of the criterion (e.g., 'Model Implementation')")
    score: Any = Field(..., description="Score for the criterion, can be a number, grade, or any value depending on rubric definition")
    score_range: List[ScoreRange] = Field(..., description="List of possible score ranges with their respective labels and descriptions")
    description: str = Field(..., description="Description of performance at the given score")

class Rubric(BaseModel):
    criteria: List[RubricCriterion] = Field(..., description="List of all criteria evaluated in the rubric")
    total_score: Any = Field(..., description="Total score achieved across all criteria, flexible for different scoring systems")
    max_total_score: Any = Field(..., description="Maximum possible total score across all criteria, flexible for different scoring systems")