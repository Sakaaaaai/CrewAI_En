import os
import yaml
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

load_dotenv()

llm = LLM(model="gemini/gemini-flash-latest")

# Load the YAML files (leave this as is)
with open("config/agents.yaml", encoding="utf-8") as f:
    agents_config = yaml.safe_load(f)
with open("config/tasks.yaml", encoding="utf-8") as f:
    tasks_config = yaml.safe_load(f)

# --- Exercise: build the Agents / Tasks from the YAML definitions ---
# Key point: the "content" of the roles and instructions lives in YAML (config), while the
#            Python (code) side focuses purely on assembly.
#            -> Even a non-engineer can tune the agents by editing YAML (separation of code and config)

# TODO: 1. Build researcher / writer from agents_config
#   Passing a dict to Agent(config=...) sets role/goal/backstory from it
# researcher = Agent(config=agents_config["researcher"], llm=llm, verbose=True)
# writer = Agent(config=agents_config["writer"], llm=llm, verbose=True)

# TODO: 2. Build research_task / write_task from tasks_config
#   Passing a dict to Task(config=...) sets description/expected_output
#   agent and context (data hand-off) are specified on the Python side
# research_task = Task(config=tasks_config["research_task"], agent=researcher)
# write_task = Task(config=tasks_config["write_task"], agent=writer, context=[research_task])

# TODO: 3. Assemble the Crew and run it
# crew = Crew(
#     agents=[researcher, writer],
#     tasks=[research_task, write_task],
#     process=Process.sequential,
#     verbose=True,
# )
# result = crew.kickoff(inputs={"topic": "renewable energy"})

print("\n=== Article ===")
print(result)

# TODO: 4. Rewrite the backstory in config/agents.yaml (e.g. change the tone), and confirm
#           the output changes without touching a single line of exercise.py
