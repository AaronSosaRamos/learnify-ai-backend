#from app.api.features.schemas.schemas import RequestSchema, SpellingCheckerRequestArgs
from fastapi import APIRouter, Depends
from app.api.logger import setup_logger
from app.api.auth.auth import key_check

logger = setup_logger(__name__)
router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

# @router.post("/check-spelling")
# async def submit_tool( data: RequestSchema, _ = Depends(key_check)):
#     logger.info(f"Loading request args...")
#     args = SpellingCheckerRequestArgs(spelling_checker_schema=data)
#     logger.info(f"Args. loaded successfully")

#     chain = compile_chain()

#     logger.info("Generating the spelling checking analysis")
#     results = chain.invoke(args.validate_and_return())
#     logger.info("The spelling checking analysis has been successfully generated")

#     return results