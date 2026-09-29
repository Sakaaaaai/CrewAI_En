import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM

load_dotenv()

llm = LLM(model="gemini/gemini-flash-latest")

# Agent is already set up (leave this as is; covered in 1-2)
writer = Agent(
    role="Copywriter",
    goal="Write copy that conveys the appeal of a product",
    backstory="You are a professional copywriter who is great at capturing hearts with just a few words.",
    llm=llm,
    verbose=True,
)


# --- The star of this exercise: defining a Task ---
# TODO: 1. Define a Task that introduces a "newly launched coffee"
#   description     … the instructions given to the agent (what you want it to do)
#   expected_output … the shape of the deliverable you expect. The more specific this is, the more stable the output
# task = Task(
#     description="Write a piece of copy introducing our newly launched hot coffee, 'Morning Cup'.",
#     expected_output="",   # <- start by setting this to "a one-line tagline"
#     agent=writer,
# )

crew = Crew(agents=[writer], tasks=[task])
result = crew.kickoff()

print("\n=== Result ===")
print(result)

# TODO: 2. Change expected_output and run it again to compare the results
#   1st run: expected_output="a one-line tagline"
#   2nd run: expected_output="an ~100-word introduction that includes 3 emoji"
#   -> Confirm that even with the same description (instructions), changing the
#      expected shape of the output changes the result
