from typing import List
import os

from app.api.features.schemas.ai_resistant_schemas import AIResistantOutput
from app.api.logger import setup_logger
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import GoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

relative_path = "features/quzzify"

logger = setup_logger(__name__)

def read_text_file(file_path):
    # Get the directory containing the script file
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Combine the script directory with the relative file path
    absolute_file_path = os.path.join(script_dir, file_path)
    
    with open(absolute_file_path, 'r') as file:
        return file.read()
    
class AIResistantAssignmentGenerator:
    def __init__(self, args=None, vectorstore_class=Chroma, prompt=None, embedding_model=None, model=None, parser=None, verbose=False):
        default_config = {
            "model": GoogleGenerativeAI(model="gemini-1.5-flash"),
            "embedding_model": GoogleGenerativeAIEmbeddings(model='models/embedding-001'),
            "parser": JsonOutputParser(pydantic_object=AIResistantOutput),
            "prompt": read_text_file("prompt/ai-resistant-prompt.txt"),
            "vectorstore_class": Chroma
        }

        self.prompt = prompt or default_config["prompt"]
        self.model = model or default_config["model"]
        self.parser = parser or default_config["parser"]
        self.embedding_model = embedding_model or default_config["embedding_model"]

        self.vectorstore_class = vectorstore_class or default_config["vectorstore_class"]
        self.vectorstore, self.retriever, self.runner = None, None, None
        self.args = args
        self.verbose = verbose

        if vectorstore_class is None: raise ValueError("Vectorstore must be provided")
        if args.topic is None: raise ValueError("Topic must be provided")
        if args.assignment is None: raise ValueError("Assignment must be provided")
        if args.grade_level is None: raise ValueError("Grade Level must be provided")
        if args.grade_level is None: raise ValueError("Language must be provided")


    def compile(self, documents: List[Document]):
        # Return the chain
        prompt = PromptTemplate(
            template=self.prompt,
            input_variables=["attribute_collection"],
            partial_variables={"format_instructions": self.parser.get_format_instructions()}
        )

        if self.runner is None:
            logger.info(f"Creating vectorstore from {len(documents)} documents") if self.verbose else None
            self.vectorstore = self.vectorstore_class.from_documents(documents, self.embedding_model)
            logger.info(f"Vectorstore created") if self.verbose else None

            self.retriever = self.vectorstore.as_retriever()
            logger.info(f"Retriever created successfully") if self.verbose else None

            self.runner = RunnableParallel(
                {"context": self.retriever,
                "attribute_collection": RunnablePassthrough()
                }
            )

        chain = self.runner | prompt | self.model | self.parser

        if self.verbose: logger.info(f"Chain compilation complete")

        return chain

    def create_assignments(self, documents: List[Document]):
        if self.verbose: logger.info(f"Creating the AI-Resistant assignments")

        chain = self.compile(documents)

        response = chain.invoke(f"Topic: {self.args.topic}, Assignment: {self.args.assignment}, Grade Level: {self.args.grade_level}, Language (YOU MUST RESPOND IN THIS LANGUAGE): {self.args.lang}")

        if self.verbose: logger.info(f"Deleting vectorstore")
        self.vectorstore.delete_collection()

        return response