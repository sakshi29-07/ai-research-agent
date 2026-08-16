from agents.research_agent import research_agent, evaluate_result 
question = "Explain what an AI Research Agent is."
answer = research_agent(question)
print(answer)
print(evaluate_result(answer))