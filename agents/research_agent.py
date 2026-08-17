import logging
import os
import re

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from tools.research_tool import research_tool
from tools.calculator_tool import calculator_tool


logging.basicConfig(level=logging.INFO)

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")

model = ChatOpenAI(
    model=MODEL_NAME,
    temperature=0
)


def research_agent(question):
    logging.info("Research agent started")

    # Validate question
    if not question or not question.strip():
        return {
            "status": "error",
            "message": "Question cannot be empty."
        }

    question_lower = question.lower()

    # -------------------------
    # Calculator Tool
    # -------------------------

    calculation_keywords = (
        "calculate",
        "multiply",
        "add",
        "subtract",
        "divide"
    )

    if any(keyword in question_lower for keyword in calculation_keywords):

        numbers = re.findall(r"\d+", question)
        numbers = [int(num) for num in numbers]

        if len(numbers) < 2:
            return {
                "question": question,
                "status": "error",
                "message": "Please provide two numbers for calculation."
            }

        if "multiply" in question_lower:
            operation = "multiply"
        elif "add" in question_lower:
            operation = "add"
        elif "subtract" in question_lower:
            operation = "subtract"
        elif "divide" in question_lower:
            operation = "divide"
        else:
            return {
                "question": question,
                "status": "error",
                "message": "Please specify an operation."
            }

        try:
            calculation_result = calculator_tool(
                numbers[0],
                numbers[1],
                operation
            )

            return {
                "question": question,
                "result": calculation_result,
                "status": "completed",
                "mode": "calculator"
            }

        except Exception as e:
            return {
                "question": question,
                "status": "error",
                "message": f"Calculation failed: {e}"
            }

    # -------------------------
    # Research Tool
    # -------------------------

    try:
        research_result = research_tool(question)
        logging.info("Research tool completed successfully")

    except Exception as e:
        return {
            "question": question,
            "status": "error",
            "message": f"Research failed: {e}"
        }

    # -------------------------
    # LLM
    # -------------------------

    prompt = f"""
    You are an AI research assistant.

    Based on the research information below, answer the user's question clearly.

    Question:
    {question}

    Research information:
    {research_result}
    """

    try:
        response = model.invoke(prompt)

        return {
            "question": question,
            "research": research_result,
            "answer": response.content,
            "status": "completed",
            "mode": "llm"
        }

    except Exception as e:
        logging.warning("LLM unavailable: %s", e)

        return {
            "question": question,
            "research": research_result,
            "status": "completed",
            "mode": "research_only",
            "message": f"LLM unavailable: {e}"
        }


def evaluate_result(result):

    if not result:
        return "Evaluation failed"

    if result.get("status") == "error":
        return "Evaluation failed: agent returned an error"

    if result.get("mode") == "llm":
        return "Evaluation passed: LLM answer generated successfully."

    if result.get("mode") == "research_only":
        return "Evaluation passed: research available, LLM unavailable."

    if result.get("mode") == "calculator":
        return "Evaluation passed: calculator tool used successfully."

    return "Evaluation failed: no valid result found"