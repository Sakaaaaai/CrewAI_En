import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

load_dotenv()

llm = LLM(model="gemini/gemini-flash-latest")

# Researcher + writer from 2-2 (leave this as is)
researcher = Agent(
    role="Researcher",
    goal="Accurately research the key points of {topic}",
    backstory="You are a research expert who is great at quickly spotting the key points.",
    llm=llm, verbose=True,
)
writer = Agent(
    role="Writer",
    goal="Write an easy-to-understand introduction based on the research results",
    backstory="You are a writer who is great at conveying difficult content in a simple, approachable way.",
    llm=llm, verbose=True,
)

# TODO: 1. Define the "editor" Agent
#   Role: take the writer's text and polish it into a final draft, fixing mistakes and awkward phrasing
# editor = Agent(
#     role="Editor",
#     goal="Proofread the text and turn it into a polished, accurate final draft",
#     backstory="You are a veteran editor with a sharp eye for detail. Nothing gets past you — typos or awkward phrasing.",
#     llm=llm, verbose=True,
# )

research_task = Task(
    description="Research 3 key points about {topic} for beginners.",
    expected_output="A research result with 3 bullet points",
    agent=researcher,
)
write_task = Task(
    description="Based on the research results, write an ~200-word introduction to {topic}.",
    expected_output="An ~200-word introduction",
    agent=writer,
    context=[research_task],
)

# TODO: 2. Define the proofreading task (receive the writer's text via context)
# edit_task = Task(
#     description="Proofread the writer's introduction and polish it into a more readable, accurate final draft.",
#     expected_output="The proofread final draft",
#     agent=editor,
#     context=[write_task],
# )

# TODO: 3. Assemble and run a Crew with 3 agents and 3 tasks
# crew = Crew(
#     agents=[researcher, writer, editor],
#     tasks=[research_task, write_task, edit_task],
#     process=Process.sequential,
#     verbose=True,
# )
# result = crew.kickoff(inputs={"topic": "the science of sleep"})

print("\n=== Final draft (polished by the editor) ===")
print(result)
