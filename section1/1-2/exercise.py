import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM

load_dotenv()

# The LLM we'll use (leave this as is)
llm = LLM(model="gemini/gemini-flash-latest")


# --- The star of this exercise: defining an Agent ---
# TODO: 1. Define a "researcher" Agent
#   role      … the person's title/role (e.g. "Technology Researcher")
#   goal      … what they want to achieve (e.g. "produce accurate research that beginners can understand")
#   backstory … their persona. This is what shapes tone and perspective the most (e.g. "You are an expert researcher with 10 years of experience…")
# researcher = Agent(
#     role="",
#     goal="",
#     backstory="",
#     llm=llm,
#     verbose=True,
# )


# Task and Crew for testing (leave these as is)
# NOTE: An Agent alone doesn't produce output. It needs a Task to run inside a Crew (more on this in 1-3, 1-4)
task = Task(
    description="Explain what an 'AI agent' is in three sentences.",
    expected_output="A 3-sentence explanation",
    agent=researcher,  # <- uses the researcher you defined above
)

crew = Crew(agents=[researcher], tasks=[task])
result = crew.kickoff()

print("\n=== Result ===")
print(result)

# TODO: 2. Rewrite the backstory as something like "a teacher who explains things
#           so a child can understand" and see how the tone of the output changes
#           (feel free to change role / goal too)
