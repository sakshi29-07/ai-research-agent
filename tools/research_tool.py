def research_tool(topic):
    """Performs a basic research operation for a given topic."""
    result =f"Research requested for: {topic}"
    # return result

    research_data = {
        "topic":topic,
        "status":"research completed",
        "summary":f"Basic research information collected for.{topic}",
        "sources":[
            "Python documentation",
            "LangChain documentation",
            "LangGraph documentation"
        ]
    }

    return research_data 