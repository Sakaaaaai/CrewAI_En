import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

load_dotenv()

llm = LLM(model="gemini/gemini-flash-latest")

# Researcher (leave this as is)
researcher = Agent(
    role="Researcher",
    goal="Accurately research the key points of {topic}",
    backstory="You are a research expert who is great at quickly spotting the key points.",
    llm=llm,
    verbose=True,
)

# TODO: 1. Define the Writer Agent
#   Role: take the research results and turn them into an easy-to-read introduction
# writer = Agent(
#     role="Writer",
#     goal="Write an easy-to-understand introduction based on the research results",
#     backstory="You are a writer who is great at conveying difficult content in a simple, approachable way.",
#     llm=llm,
#     verbose=True,
# )

# Research task (leave this as is)
research_task = Task(
    description="Research 3 key points about {topic} for beginners.",
    expected_output="A research result with 3 bullet points",
    agent=researcher,
)

# TODO: 2. Define the writing task
#   Specifying context=[research_task] passes the research output into this task (handoff from one stage to the next)
# write_task = Task(
#     description="Based on the research results, write an ~200-word introduction to {topic}.",
#     expected_output="An ~200-word introduction",
#     agent=writer,
#     context=[research_task],
# )

# TODO: 3. Assemble a Crew from the 2 agents and 2 tasks (run in order)
# crew = Crew(
#     agents=[researcher, writer],
#     tasks=[research_task, write_task],
#     process=Process.sequential,
#     verbose=True,
# )

# result = crew.kickoff(inputs={"topic": "deep-sea creatures"})

print("\n=== Final deliverable (introduction) ===")
print(result)
