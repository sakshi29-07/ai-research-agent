from agents.research_agent import research_agent, evaluate_result 
question = "Python"
answer = research_agent(question)
print(answer)
print(evaluate_result(answer))