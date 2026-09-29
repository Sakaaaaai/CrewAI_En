import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import FileReadTool

load_dotenv()

llm = LLM(model="gemini/gemini-flash-latest")

# File-reading tool (leave this as is)
file_tool = FileReadTool()

# TODO: 1. Define a "researcher" Agent that reads memo.txt (equip it with file_tool)
# reader = Agent(
#     role="Researcher",
#     goal="Read a scrawled memo and organize the key points",
#     backstory="You are skilled at picking out the important information from a messy memo.",
#     tools=[file_tool],
#     llm=llm,
#     verbose=True,
# )

# TODO: 2. Define a "writer" Agent that writes a polished report (no tool needed)
# writer = Agent(
#     role="Business Writer",
#     goal="Turn organized information into a readable report",
#     backstory="You are a professional at turning bullet-point memos into a well-formatted proposal.",
#     llm=llm,
#     verbose=True,
# )

# TODO: 3. A task that "reads memo.txt and organizes the key points"
# read_task = Task(
#     description="Read memo.txt and organize the new product idea into 'Features,' 'Target audience,' and 'Open issues.'",
#     expected_output="Bullet points organized into 3 categories",
#     agent=reader,
# )

# TODO: 4. A task that "turns the organized results into a report" (receives read_task via context)
# write_task = Task(
#     description="Based on the organized information, create a proposal report (Markdown) with headings.",
#     expected_output="# A proposal report (Markdown) with headings",
#     agent=writer,
#     context=[read_task],
#     output_file="proposal.md",
# )

# TODO: 5. Assemble and run a Crew with the 2 agents and 2 tasks
# crew = Crew(
#     agents=[reader, writer],
#     tasks=[read_task, write_task],
#     process=Process.sequential,
#     verbose=True,
# )
# result = crew.kickoff()

print("\n=== Proposal Report ===")
print(result)
print("\n-> proposal.md has been generated.")
