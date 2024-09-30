from app.api.features.ai_resistant_service import AIResistantAssignmentGenerator
from app.api.features.ai_rubric_generator import RubricGenerator
from app.api.features.document_loaders import get_docs
from app.api.features.personalized_tasks_service import AIConnectWithThemGenerator
from app.api.features.schemas.ai_resistant_schemas import AIResistantArgs
from app.api.features.schemas.ai_rubric_generator_schemas import RubricGeneratorArgs
from app.api.features.schemas.personalized_tasks_schemas import ConnectWithThemArgs
from fastapi import APIRouter, Depends
from app.api.logger import setup_logger
from app.api.auth.auth import key_check

logger = setup_logger(__name__)
router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.post("/ai-resistant-assignments")
async def submit_tool( data: AIResistantArgs, _ = Depends(key_check)):
    try:
        logger.info(f"File URL loaded: {data.file_url}")

        docs = get_docs(data.file_url, data.file_type, True)
    
        output = AIResistantAssignmentGenerator(args=data, verbose=True).create_assignments(docs)
    
    except Exception as e:
        error_message = f"Error in executor: {e}"
        logger.error(error_message)
        raise ValueError(error_message)
    
    return output

@router.post("/personalized-tasks")
async def submit_tool( data: ConnectWithThemArgs, _ = Depends(key_check)):
    try:
        logger.info(f"File URL loaded: {data.file_url}")

        docs = get_docs(data.file_url, data.file_type, True)
    
        output = AIConnectWithThemGenerator(args=data, verbose=True).generate_suggestion(docs)
    
    except Exception as e:
        error_message = f"Error in executor: {e}"
        logger.error(error_message)
        raise ValueError(error_message)
    
    return output

@router.post("/ai-rubric-generator")
async def submit_tool( data: RubricGeneratorArgs, _ = Depends(key_check)):
    try:
        logger.info(f"File URL loaded: {data.file_url}")

        docs = get_docs(data.file_url, data.file_type, True)
    
        output = RubricGenerator(args=data, verbose=True).generate_rubric(docs)
    
    except Exception as e:
        error_message = f"Error in executor: {e}"
        logger.error(error_message)
        raise ValueError(error_message)
    
    return output