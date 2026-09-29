"""Smoke test (minimal check that dependencies install and Gemini responds).

Usage (in the CodeSandbox terminal, at the repository root):
    pip install -r requirements.txt
    python smoke_test.py

Set your API key first, either as the GOOGLE_API_KEY env variable or in a .env file.
This also confirms that the `crewai[google-genai]` extra took effect.
Once you've confirmed things work, you can delete this file (it isn't needed for the exercises).
"""
import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()
assert os.environ.get("GOOGLE_API_KEY"), \
    "GOOGLE_API_KEY is not set (check your Env Variables or .env)"

llm = LLM(model="gemini/gemini-flash-latest")
res = llm.call("Reply with exactly: Setup OK")

print("Response:", res)
print("CrewAI x Gemini call succeeded (the google-genai extra is active). You're ready to start the exercises.")
