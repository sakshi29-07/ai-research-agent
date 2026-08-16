import logging
logging.basicConfig(level=logging.INFO)
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from tools.research_tool import research_tool
load_dotenv()
MODEL_NAME=os.getenv("MODEL_NAME","gpt-4o-mini")

model = ChatOpenAI(
    model="MODEL_NAME",
    temperature=0
)

def research_agent(question) :
    logging.info("Research agent started")
    if not question or not question.strip():
        return{
            "status":"error",
            "message":"Question cannot be empty."
            
        }
    try:
        research_result = research_tool(question)
        logging.info("Research tool completed successfully")
    except Exception as e:
        return{
            "status": "error",
            "message": f"Research failed: {e}"
        }    

   # return research_result
    prompt = f"""
    You are an AI research assistant.
    Based on the research information below, answer the user's question clearly
    Question:
    {question}
    Research information:
    {research_result}
    """
    return {
       "question": question,
       "research": research_result,
       "status": "completed",
       "mode":"offline_test"
           }
def evaluate_result(result):
    if not result:
        return "Evaluation failed"
    if result.get("status")=="error":
        return "Evaluation failed: agent returned an error"
    if result.get("research"):
        return "Evaluation passed: research result is available"
    return "Evaluation failed: no research result found"