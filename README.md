# AI Research Agent

An AI research agent built using Python, LangChain, OpenAI, and external tools.

## Features

- Researches user questions using the Wikipedia API
- Uses a calculator tool for arithmetic operations
- Supports addition, subtraction, multiplication, and division
- Selects a tool based on the user's question
- Input validation and error handling
- LLM-based response generation
- Fallback mode when the LLM is unavailable
- Result evaluation

## Architecture

User Question
      |
      v
Research Agent
      |
      +------ Calculator Tool
      |
      +------ Research Tool ------> Wikipedia API
                     |
                     v
                    LLM
                     |
                     v
               Final Response

## Technologies

- Python
- LangChain
- OpenAI
- Requests
- Wikipedia API
- python-dotenv

## Project Structure

ai-research-agent/
│
├── main.py
├── agents/
│   └── research_agent.py
├── tools/
│   ├── research_tool.py
│   └── calculator_tool.py
├── .env
├── .gitignore
└── requirements.txt

## Example

Input:

multiply 10 and 5

Output:

50

## Error Handling

The agent handles:

- Empty questions
- Missing numbers
- Invalid calculation requests
- Division by zero
- Research API failures
- LLM/API failures

## Future Improvements

- Add more tools
- Use an LLM for dynamic tool selection
- Add conversation memory
- Add LangGraph workflow
- Add more advanced evaluation