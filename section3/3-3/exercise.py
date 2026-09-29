import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai.tools import tool

load_dotenv()

llm = LLM(model="gemini/gemini-flash-latest")


# --- Example: a custom tool (leave this as is) ---
# The @tool decorator turns a function into a tool.
# The """ docstring """ becomes the explanation of "what this tool does," which the agent uses to decide how to use it.
@tool("Sales Tax Calculator")
def calc_tax(price: int) -> str:
    """Takes a pre-tax price (an integer) and returns the price with 10% sales tax added"""
    return f"The price including tax is {int(price * 1.1)} yen"


# --- Exercise: build your own character-count tool ---
# TODO: 1. Use @tool to create a "character count" tool
#   - It takes a string and returns its character count
#   - Always write in the docstring what the tool does (this is the explanation given to the agent)
# @tool("Character Count")
# def count_chars(text: str) -> str:
#     """Counts the number of characters in the given text and returns it"""
#     return f"{len(text)} characters"


# TODO: 2. Define a writer Agent equipped with the character-count tool
# writer = Agent(
#     role="Copywriter",
#     goal="Write a tagline that is exactly a specified number of characters",
#     backstory="You are a professional copywriter who carefully chooses words with an eye on character count.",
#     tools=[count_chars],
#     llm=llm,
#     verbose=True,
# )

# TODO: 3. Define a task that "creates a tagline that is exactly 20 characters long"
#   The agent will use the count_chars tool to check the length of what it writes and adjust it
# task = Task(
#     description="Write a tagline that is exactly 20 characters long for the new water bottle product, "
#                 "'Forever Cool Bottle'. "
#                 "Check the length with the character-count tool as you go, and adjust it to exactly 20 characters.",
#     expected_output="A tagline that is exactly 20 characters long",
#     agent=writer,
# )

crew = Crew(agents=[writer], tasks=[task], process=Process.sequential, verbose=True)
result = crew.kickoff()

print("\n=== Tagline ===")
print(result)
