# LearnifyAI Backend

**LearnifyAI Backend** is a sophisticated backend system that powers the LearnifyAI platform. It provides four core services, leveraging AI and multimodal capabilities to assist educators in syllabus creation, assignment generation, task personalization, and rubric creation. The backend is designed to handle requests in a highly efficient manner by utilizing RAG (Retrieval-Augmented Generation) pipelines and Large Language Models (LLMs) to provide accurate and context-aware responses in JSON format.

Developed by **Wilfredo Aaron Sosa Ramos**, the system integrates various AI technologies such as LangChain, ChromaDB, and Google Generative AI to deliver fast, relevant, and insightful responses to educational tasks.

## Table of Contents

- [1. Features](#1-features)
- [2. Services Provided](#2-services-provided)
  - [2.1 AI Syllabus Generator](#21-ai-syllabus-generator)
  - [2.2 AI-Resistant Assignments](#22-ai-resistant-assignments)
  - [2.3 Personalized Tasks](#23-personalized-tasks)
  - [2.4 AI Rubric Generator](#24-ai-rubric-generator)
- [3. RAG Pipelines](#3-rag-pipelines)
- [4. Multimodal Capabilities](#4-multimodal-capabilities)
- [5. Technologies Used](#5-technologies-used)
- [6. Installation Guide](#6-installation-guide)
- [7. How to Use](#7-how-to-use)

---

## 1. Features

The **LearnifyAI Backend** offers the following key features:

- **AI-Powered Educational Services**: Provides four core educational services to assist educators in syllabus generation, assignment creation, task personalization, and rubric development.
- **RAG Pipelines**: Uses Retrieval-Augmented Generation (RAG) pipelines to enhance the quality of AI-generated content by retrieving relevant information from a Vector DB.
- **Multimodal Support**: Capable of processing over 16 different file types (PDF, TXT, WORD, EXCEL, images, YouTube videos, and more), ensuring robust support for diverse content.
- **Few-Shot Approach**: Uses few-shot learning in LLMs to generate accurate and tailored responses based on limited examples, delivered in JSON format.

These features enable educators to automate and enhance key aspects of the learning process through AI-powered solutions.

---

## 2. Services Provided

The **LearnifyAI Backend** delivers four primary services to streamline and enhance the educational experience:

### 2.1 AI Syllabus Generator

The **AI Syllabus Generator** helps educators create comprehensive and customizable syllabi. It supports:

- **Automatic Syllabus Creation**: Generates syllabi based on course details, learning objectives, and timelines.
- **Customizable Sections**: Allows for customization of course materials, weekly breakdowns, and assessment strategies.
- **Few-Shot AI Support**: Uses a few-shot approach to ensure the generated syllabus is tailored to specific academic needs.

### 2.2 AI-Resistant Assignments

The **AI-Resistant Assignments** service helps educators design assignments that are challenging for AI-based cheating tools. Features include:

- **Assignment Creation**: Automatically generates assignments with high resistance to AI-generated solutions.
- **Custom Task Generation**: Provides a flexible framework for creating assignments that promote critical thinking.
- **Content Verification**: Ensures the assignment content is relevant and up-to-date.

### 2.3 Personalized Tasks

The **Personalized Tasks** service generates custom learning tasks based on individual student needs. It includes:

- **Student-Centered Task Generation**: Customizes learning tasks based on the student’s performance, learning style, and progress.
- **Dynamic Updates**: Continuously updates tasks based on student feedback and evolving academic requirements.
- **Content Adaptability**: Provides tailored recommendations and learning materials from various sources, ensuring personalized learning paths.

### 2.4 AI Rubric Generator

The **AI Rubric Generator** assists educators in creating detailed grading rubrics. Key features include:

- **Rubric Creation**: Automatically generates detailed rubrics for specific assignments or learning objectives.
- **Criteria Customization**: Allows educators to customize the criteria for evaluating student work.
- **Few-Shot Learning**: Ensures that the generated rubrics are tailored to specific assignments, following a few-shot approach for accuracy and relevance.

---

## 3. RAG Pipelines

The **LearnifyAI Backend** uses **Retrieval-Augmented Generation (RAG)** pipelines to provide accurate and context-aware responses. Each pipeline follows this structure:

1. **Prompt**: A user’s input, such as a request for syllabus generation or assignment creation, triggers the pipeline.
2. **Vector DB (ChromaDB)**: Relevant documents and content are retrieved from a vector database (ChromaDB), which stores data in a vectorized format.
3. **Retriever**: The retriever fetches the most relevant information from the Vector DB, narrowing down the context.
4. **LLM (Large Language Model)**: The retriever’s output is fed into the LLM (powered by Google Generative AI), which generates the content or response based on the retrieved data.
5. **Parser**: The generated response is parsed and formatted into a structured JSON output.

These pipelines ensure that responses are not only generated using AI but are also contextually accurate and relevant, thanks to the retrieval of relevant data.

---

## 4. Multimodal Capabilities

The **LearnifyAI Backend** supports over 16 different file types, ensuring it can process and generate responses based on a wide variety of content formats. Supported formats include:

- **Document Files**: PDF, TXT, WORD, EXCEL
- **Images**: PNG, JPG, GIF
- **Media**: YouTube Videos, MP4
- **Data Files**: CSV, JSON
- **Other**: Markdown, LaTeX

This multimodal support allows educators to input diverse types of content and receive relevant, context-aware responses from the AI.

---

## 5. Technologies Used

The **LearnifyAI Backend** leverages a powerful tech stack to provide intelligent, contextually aware educational solutions:

- **Python**: A versatile programming language that powers the backend services.
- **FastAPI**: A modern, fast web framework for building APIs with Python.
- **LangChain**: A framework used to build LLM applications with support for complex AI workflows.
- **ChromaDB**: A vector database that powers the retrieval of relevant content for the RAG pipelines.
- **Google Generative AI**: Powers the LLM responses, providing accurate, context-driven content generation.
- **RAG Pipelines**: Combines retrieval-based AI with generation to deliver high-quality outputs in a few-shot format.

---

## 6. Installation Guide

Follow these steps to set up and run the **LearnifyAI Backend** locally:

1. **Clone the repository**:
   - Clone the repository to your local machine using the following command:
     ```
     git clone https://github.com/yourusername/LearnifyAIBackend.git
     ```

2. **Navigate to the project directory**:
   - Move into the project folder:
     ```
     cd LearnifyAIBackend
     ```

3. **Set up a virtual environment** (optional but recommended):
   - Create a virtual environment and activate it:
     ```
     python -m venv venv
     source venv/bin/activate
     ```

4. **Install dependencies**:
   - Install the required Python packages using pip:
     ```
     pip install -r requirements.txt
     ```

5. **Run the development server**:
   - Start the FastAPI server locally:
     ```
     uvicorn app.main:app --host 0.0.0.0 --port 8000
     ```

6. **Test the API**:
   - Visit `http://localhost:8000/docs` to view the interactive API documentation powered by Swagger UI.

---

## 7. How to Use

Once the **LearnifyAI Backend** is set up, you can access its services by making requests to the provided API endpoints. Here’s a brief overview of how to use each service:

1. **AI Syllabus Generator**:
   - Send a request with course details, learning objectives, and timeline information to the syllabus generation endpoint. The service will return a JSON response with a detailed syllabus.

2. **AI-Resistant Assignments**:
   - Provide assignment parameters and the system will generate assignments that are resistant to AI-based cheating tools. The response will be formatted in JSON.

3. **Personalized Tasks**:
   - Input student-specific data (performance, learning style, etc.), and the service will return personalized learning tasks tailored to individual needs.

4. **AI Rubric Generator**:
   - Send assignment details, and the service will return a JSON-formatted grading rubric based on a few-shot approach.

Throughout the process, responses will be provided in a structured JSON format, ensuring clarity and ease of use for developers and educators alike.

