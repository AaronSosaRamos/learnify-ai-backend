from typing import List, Optional
from pydantic import BaseModel, Field

class SyllabusGeneratorArgsModel(BaseModel):
    grade_level: str
    course: str
    instructor_name: str
    instructor_title: str
    unit_time: str
    unit_time_value: int
    start_date: str
    start_date: str
    assessment_methods: str
    grading_scale: str
    file_url: str
    file_type: str
    lang: Optional[str] = "en"

class CourseInformation(BaseModel):
    course_title: str = Field(description="The course title")
    grade_level: str = Field(description="The grade level")
    description: str = Field(description="The course description")

class InstructorInformation(BaseModel):
    name: str = Field(description="The instructor name")
    title: str = Field(description="The instructor title")
    description_title: str = Field(description="The description of the instructor title")

class CourseDescriptionObjectives(BaseModel):
    objectives: List[str] = Field(description="The course objectives")
    intended_learning_outcomes: List[str] = Field(description="The intended learning outcomes of the course")

class CourseContentItem(BaseModel):
    unit_time: str = Field(description="The unit of time for the course content")
    unit_time_value: int = Field(description="The unit of time value for the course content")
    topic: str = Field(description="The topic per unit of time for the course content")

class PoliciesProcedures(BaseModel):
    attendance_policy: str = Field(description="The attendance policy of the class")
    late_submission_policy: str = Field(description="The late submission policy of the class")
    academic_honesty: str = Field(description="The academic honesty policy of the class")

class AssessmentMethod(BaseModel):
    type_assessment: str = Field(description="The type of assessment")
    weight: int = Field(description="The weight of the assessment in the final grade")

class AssessmentGradingCriteria(BaseModel):
    assessment_methods: List[AssessmentMethod] = Field(description="The assessment methods")
    grading_scale: dict = Field(description="The grading scale")

class LearningResource(BaseModel):
    title: str = Field(description="The book title of the learning resource")
    author: str = Field(description="The book author of the learning resource")
    year: int = Field(description="The year of creation of the book")

class CourseScheduleItem(BaseModel):
    unit_time: str = Field(description="The unit of time for the course schedule item")
    unit_time_value: int = Field(description="The unit of time value for the course schedule item")
    date: str = Field(description="The date for the course schedule item")
    topic: str = Field(description="The topic for the learning resource")
    activity_desc: str = Field(description="The descrition of the activity for the learning resource")

class SyllabusSchema(BaseModel):
    course_information: CourseInformation = Field(description="The course information")
    instructor_information: InstructorInformation = Field(description="The instructor information")
    course_description_objectives: CourseDescriptionObjectives = Field(description="The objectives of the course")
    course_content: List[CourseContentItem] = Field(description="The content of the course")
    policies_procedures: PoliciesProcedures = Field(description="The policies procedures of the course")
    assessment_grading_criteria: AssessmentGradingCriteria = Field(description="The asssessment grading criteria of the course")
    learning_resources: List[LearningResource] = Field(description="The learning resources of the course")
    course_schedule: List[CourseScheduleItem] = Field(description="The course schedule")

class SyllabusRequestArgs:
    def __init__(self, 
                 syllabus_generator_args: SyllabusGeneratorArgsModel,
                 summary: str):

        self._grade_level = syllabus_generator_args.grade_level
        self._course = syllabus_generator_args.course
        self._instructor_name = syllabus_generator_args.instructor_name
        self._instructor_title = syllabus_generator_args.instructor_title
        self._unit_time = syllabus_generator_args.unit_time
        self._unit_time_value = syllabus_generator_args.unit_time_value
        self._start_date = syllabus_generator_args.start_date
        self._assessment_methods = syllabus_generator_args.assessment_methods
        self._grading_scale = syllabus_generator_args.grading_scale
        self._lang = syllabus_generator_args.lang
        self._summary = summary

    @property
    def grade_level(self) -> str:
        return self._grade_level

    @property
    def course(self) -> str:
        return self._course

    @property
    def instructor_name(self) -> str:
        return self._instructor_name

    @property
    def instructor_title(self) -> str:
        return self._instructor_title

    @property
    def unit_time(self) -> str:
        return self._unit_time

    @property
    def unit_time_value(self) -> int:
        return self._unit_time_value

    @property
    def start_date(self) -> str:
        return self._start_date

    @property
    def assessment_methods(self) -> str:
        return self._assessment_methods

    @property
    def grading_scale(self) -> str:
        return self._grading_scale

    @property
    def lang(self) -> str:
        return self._lang

    @property
    def summary(self) -> str:
        return self._summary

    def to_dict(self) -> dict:
        return {
            "grade_level": self.grade_level,
            "course": self.course,
            "instructor_name": self.instructor_name,
            "instructor_title": self.instructor_title,
            "unit_time": self.unit_time,
            "unit_time_value": self.unit_time_value,
            "start_date": self.start_date,
            "assessment_methods": self.assessment_methods,
            "grading_scale": self.grading_scale,
            "lang": self.lang,
            "summary": self.summary
        }