# tests.py

import unittest
from main import fetch_latest_news, search_agent, summary_agent, client
from openai import OpenAI
from duckduckgo_search import DDGS

class TestNewsAgents(unittest.TestCase):
   def test_ollama_connection(self):
       test_client = OpenAI(base_url="http://127.0.0.1:11434/v1", api_key="fake-key")
       response = test_client.chat.completions.create(
           model="llama3.2:latest",
           messages=[{"role": "user", "content": "test"}]
       )
       self.assertIsNotNone(response)

   def test_ddgs_search(self):
       results = fetch_latest_news("test")
       self.assertIsNotNone(results)

   def test_search_agent(self):
       response = client.run(
           agent=search_agent,
           messages=[{"role": "user", "content": "Search news about test"}]
       )
       self.assertIsNotNone(response.messages[-1]["content"])

   def test_summary_agent(self):
       response = client.run(
           agent=summary_agent, 
           messages=[{"role": "user", "content": "Summarize: Test news article"}]
       )
       self.assertIsNotNone(response.messages[-1]["content"])

if __name__ == '__main__':
   unittest.main()