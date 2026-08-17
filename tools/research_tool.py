import requests
def research_tool(topic):
    """Performs a basic research operation for a given topic."""
    
    url = "https://en.wikipedia.org/w/api.php"

    headers = {
        "User-Agent": "AIResearchAgent/1.0"
    }

    params = {
        "action": "query",
        "list": "search",
        "srsearch": f"{topic} programming language",
        "format": "json"
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=10
)

    if response.status_code == 200:
        data = response.json()
        search_results = data.get("query", {}).get("search", [])

        if search_results:
            summary = search_results[0].get("snippet", "No summary found.")

            for result in search_results:
                if topic.lower() in result.get("title", "").lower():
                    summary = result.get("snippet", "No summary found.")
                    break
        else:
             summary = "No summary found."
    else:
        summary = f"Request failed with status code: {response.status_code}"
        # return result

    research_data = {
        "topic":topic,
        "status":"research completed",
        "summary":summary,
        "sources":[
            "Wikipedia"
        ]
    }

    return research_data 