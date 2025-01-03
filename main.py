import reflex as rx
from duckduckgo_search import DDGS
from swarm import Swarm, Agent
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI
import os

from swarm import Swarm, Agent
from openai import OpenAI
import os

# Configure OpenAI client for local Ollama instance
test_client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="dummy-key"  # Dummy key since Ollama doesn't need a real key
)

# Initialize Swarm client
client = Swarm(client=test_client)

MODEL = "llama3.2:latest"



def fetch_latest_news(topic):
    query = f"{topic} news {datetime.now().strftime('%Y-%m')}"

    with DDGS() as search_engine:
        articles = search_engine.text(query, max_results=3)
        if articles:
            formatted_results = "\n\n".join(
                f"Title: {article['title']}\nURL: {article['href']}\nSummary: {article['body']}"
                for article in articles
            )
            return formatted_results
        return f"No news articles found on the teopics: {topic}."
    print("function")
    


search_agent = Agent(
    name="News Searcher",
    instructions="""
    You are an expert in news discovery. Your role involves:
    1. Identifying the latest and most pertinent news articles on the provided topic.
    2. Ensuring all sources are credible and trustworthy.
    3. Presenting the raw search results in a clear and organized manner.
    """,
    functions=[fetch_latest_news],
    model=MODEL
)

messages = []

search_response = client.run(
            agent=search_agent,
            messages=[{"role": "user", "content": f"Search for latest news about {"test"}"}]
)

# News Summary Agent
summary_agent = Agent(
    name="Comprehensive News Synthesizer",
    instructions="""
    You are a skilled news analyst, proficient in synthesizing multiple sources and crafting engaging, concise summaries. Your responsibilities include:

    **Synthesis and Analysis:**
    1. Review the provided news articles thoroughly, extracting key insights and essential details.
    2. Merge information from various sources into a unified narrative, ensuring factual accuracy and journalistic neutrality.
    3. Highlight the main event, key players, significant data, and context to ensure a comprehensive overview.

    **Writing Style and Delivery:**
    1. Write in a clear, active, and accessible tone that balances professionalism with readability.
    2. Simplify complex concepts for a broader audience while maintaining depth and accuracy.
    3. Use specifics over generalities, ensuring that each word adds value.

    **Deliverable:**
    Compose an engaging, multi-paragraph summary (300-400 words) with the following structure:
    - Start with the most critical development, including key players and their actions.
    - Follow with context and supporting details drawn from multiple sources.
    - Conclude with the immediate relevance, significance, and potential short-term implications.
    """,
    model=MODEL
)

# Test the agents
def test_agents(topic):
    try:
        # Test search agent
        search_response = client.run(
            agent=search_agent,
            messages=[{"role": "user", "content": f"Search for latest news about {topic}"}]
        )
        print("Search Agent Response:", search_response.messages[-1]["content"])

        # Test summary agent
        summary_response = client.run(
            agent=summary_agent,
            messages=[{"role": "user", "content": f"Summarize the following news: {search_response.messages[-1]['content']}"}]
        )
        print("\nSummary Agent Response:", summary_response.messages[-1]["content"])
        
    except Exception as e:
        print(f"Error testing agents: {str(e)}")

if __name__ == "__main__":
    test_agents("artificial intelligence")