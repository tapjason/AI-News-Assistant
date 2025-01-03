# News Analysis System
This project implements an intelligent news analysis system using AI agents to fetch and summarize recent news articles on specified topics. The system utilizes a local LLM server (Ollama) and combines web scraping with AI-powered analysis to provide comprehensive news summaries.

## Project Status
⚠️⚠️⚠️⚠️⚠️ **WORK IN PROGRESS** ⚠️⚠️⚠️⚠️⚠️

This project is currently in active development. Core functionality is being implemented and tested. Expect frequent updates and potential breaking changes.

## Future Development
The project roadmap includes several planned (maybe) enhancements:
- Web-based frontend interface for easy interaction
- Additional AI agents for specialized analysis tasks
- Enhanced visualization of news trends
- API endpoint support for integration with other services
- Improved source validation and fact-checking capabilities
- Message queue system (Redis/RabbitMQ) for async processing
- Monitoring and logging system (Prometheus/Grafana)
-Embeddings-based news clustering and recommendation
- Model performance monitoring and evaluation pipeline
- A/B testing framework for agent strategies

## Features
- Automated news fetching using DuckDuckGo search
- Two specialized AI agents:
  - News Searcher: Discovers and validates recent news articles
  - Comprehensive News Synthesizer: Creates detailed summaries from multiple sources
- Local LLM integration using Ollama
- Configurable topic-based news analysis

## Prerequisites
- Python 3.10+
- Local Ollama server running
- Active internet connection for news fetching

## Installation
1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Ensure your Ollama server is running locally (default: http://localhost:11434)

## Usage
1. Run the main script with a specific topic:
```python
python main.py
```

2. The script will:
   - Fetch recent news articles about the specified topic
   - Generate a comprehensive summary of the findings
   - Display both the raw search results and the final summary

## Example Code & Output
```python
from swarm import Swarm
topic = "artificial intelligence"
test_agents(topic)
```

### Example Output
```
Search Agent Response:
Latest News on Artificial Intelligence
- Top 15 AI Trends for 2025: Focus on sustainability and resource management
- 5 Big Advances Last Year In Artificial Intelligence: ChatGPT developments and explainable AI
- Our Predictions for AI in 2025: Apple's intelligence system and chatbot growth

Summary Agent Response:
Artificial Intelligence to Play Greater Role in Sustainability in 2025
AI advancements in 2025 are focused on resource management and efficiency across industries. 
Key developments include ChatGPT-like systems, explainable AI, and Apple's intelligence system 
impact. Growth trajectory emphasizes innovation and smart management practices.
```


## Configuration
The system uses the following default settings:
- Model: llama3.2:latest
- Max search results per query: 3
- Local LLM server URL: http://localhost:11434/v1

## Error Handling
The system includes very basic error handling for:
- Failed news searches
- API connection issues
- Invalid responses