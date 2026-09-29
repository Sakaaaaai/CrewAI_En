import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

load_dotenv()

llm = LLM(model="gemini/gemini-flash-latest")

# Agent is already set up (leave this as is)
researcher = Agent(
    role="Researcher",
    goal="Accurately research the key points of a given topic",
    backstory="You are a research expert who is great at quickly spotting the key points.",
    llm=llm,
    verbose=True,
)


# --- Exercise: assemble the Task and Crew, and pass a variable via inputs ---

# TODO: 1. Define a Task that produces a summary report
#   Writing {topic} inside description lets it be replaced via kickoff's inputs (a placeholder)
# task = Task(
#     description="Summarize the key points of {topic} into 3 bullet points for beginners.",
#     expected_output="A summary report with 3 bullet points",
#     agent=researcher,
# )

# TODO: 2. Assemble the Crew
#   agents … the list of participating Agents
#   tasks  … the list of Tasks to run
#   process=Process.sequential … run them in order, top to bottom
# crew = Crew(
#     agents=[researcher],
#     tasks=[task],
#     process=Process.sequential,
#     verbose=True,
# )

# TODO: 3. Run it, passing an actual value for {topic} via inputs
#   result = crew.kickoff(inputs={"topic": "space travel"})

print("\n=== Summary report ===")
print(result)

# TODO: 4. Change "topic" in inputs to something else (e.g. "electric vehicles")
#           and confirm you can produce a report on a different topic without changing the code
