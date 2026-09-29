import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import FileReadTool

load_dotenv()

llm = LLM(model="gemini/gemini-flash-latest")

# TODO: 1. Set up a file-reading tool
#   FileReadTool() is a built-in tool for reading local files (no API key needed)
# file_tool = FileReadTool()

# TODO: 2. Define a researcher Agent equipped with the tool
#   Passing tools=[file_tool] lets this agent read files
# researcher = Agent(
#     role="Meeting Notes Analyst",
#     goal="Read a memo file and organize the key points",
#     backstory="You are skilled at pulling out important decisions from meeting notes.",
#     tools=[file_tool],
#     llm=llm,
#     verbose=True,
# )

# TODO: 3. Define a task that "reads notes.txt and summarizes it"
#   Specifying the file name notes.txt in description makes the agent go read it with the tool
# task = Task(
#     description="Read notes.txt and summarize the content in 3 bullet points, focused on what was decided.",
#     expected_output="A 3-bullet-point summary",
#     agent=researcher,
# )

crew = Crew(agents=[researcher], tasks=[task], process=Process.sequential, verbose=True)
result = crew.kickoff()

print("\n=== Summary ===")
print(result)
