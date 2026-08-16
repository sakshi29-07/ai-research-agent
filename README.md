# AI Research Agent

An AI-powered research assistant built with Python and LangChain.

## Features

- Research tool integration
- Agent-based architecture
- Input validation and guardrails
- Error handling
- Evaluation of research results
- Logging
- Environment variable configuration
- Offline testing mode

## Project Structure

ai-research-agent/
│
├── agents/
│   └── research_agent.py
│
├── tools/
│   └── research_tool.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── .env

## Technologies

- Python
- LangChain
- OpenAI API
- Python-dotenv

## How to Run

Create a virtual environment:

```bash
python -m venv venv

Activate the virtual environment:

### Windows PowerShell

bash
.\venv\Scripts\Activate.ps1


Install the required packages:

bash
pip install -r requirements.txt


Add your API key to the `.env` file.

Then run the project:

bash
python main.py
```

## Future Improvements

- Real web search integration
- LLM-powered research summaries
- Multiple research tools
- Source verification
- Better evaluation metrics
- Human-in-the-loop approval