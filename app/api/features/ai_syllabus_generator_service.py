from http.client import HTTPException
import os

from app.api.features.schemas.ai_syllabus_generator_schemas import SyllabusSchema
from app.api.logger import setup_logger
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import GoogleGenerativeAI

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

logger = setup_logger(__name__)

def read_text_file(file_path):
    # Get the directory containing the script file
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Combine the script directory with the relative file path
    absolute_file_path = os.path.join(script_dir, file_path)
    
    with open(absolute_file_path, 'r') as file:
        return file.read()

class SyllabusGeneratorPipeline:
    def __init__(self, prompt=None, parser=None, model=None, verbose=False):
        default_config = {
            "prompt": read_text_file("prompt/syllabus_generator-prompt.txt"),
            "parser": JsonOutputParser(pydantic_object=SyllabusSchema),
            "model": GoogleGenerativeAI(model="gemini-1.5-pro")
        }
        self.prompt = prompt or default_config["prompt"]
        self.model = model or default_config["model"]
        self.parser = parser or default_config["parser"]
        self.verbose = verbose

    def compile(self):
        try:
            prompt = PromptTemplate(
                template=self.prompt,
                input_variables=[
                    "grade_level", 
                    "course",
                    "instructor_name",
                    "instructor_title",
                    "unit_time",
                    "unit_time_value",
                    "start_date",
                    "assessment_methods",
                    "grading_scale",
                    "summary"
                    ],
                partial_variables={"format_instructions": self.parser.get_format_instructions()}
            )

            chain = prompt | self.model | self.parser

            if self.verbose: logger.info(f"Chain compilation complete")

        except Exception as e:
            logger.error(f"Failed to compile LLM chain : {e}")
            raise HTTPException(status_code=500, detail=f"Failed to compile LLM chain")

        return chain
    
def generate_syllabus(request_args, verbose=True):
    try:
        pipeline = SyllabusGeneratorPipeline(verbose=verbose)
        chain = pipeline.compile()
        output = chain.invoke(request_args.to_dict())

    except Exception as e:
        logger.error(f"Failed to generate syllabus: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to generate syllabus from LLM")

    return output