import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

load_dotenv()

llm = LLM(model="gemini/gemini-flash-latest")

# The 3 agents from 2-3 (leave these as is)
researcher = Agent(role="Researcher", goal="Accurately research the key points of {topic}",
                   backstory="You are a research expert who quickly spots the key points.", llm=llm, verbose=True)
writer = Agent(role="Writer", goal="Write an easy-to-understand introduction based on the research findings",
               backstory="You are a writer who explains difficult content in simple terms.", llm=llm, verbose=True)
editor = Agent(role="Editor", goal="Proofread the text and finish it into a readable final draft",
               backstory="You are a veteran editor with a keen eye for detail.", llm=llm, verbose=True)

research_task = Task(
    description="Research 3 beginner-friendly key points about {topic}.",
    expected_output="Research findings as 3 bullet points", agent=researcher,
)
write_task = Task(
    description="Based on the research findings, write a roughly 200-word introduction to {topic}.",
    expected_output="A roughly 200-word introduction", agent=writer, context=[research_task],
)

# TODO: 1. Add output_file to the proofreading task so the result is saved to a Markdown file
#   Specifying output_file="report.md" automatically writes the final output to a file
# edit_task = Task(
#     description="Proofread the writer's introduction and finish it as a Markdown article (with a heading).",
#     expected_output="# A Markdown article with a heading",
#     agent=editor,
#     context=[write_task],
#     output_file="report.md",
# )

crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[research_task, write_task, edit_task],
    process=Process.sequential,
    verbose=True,
)
result = crew.kickoff(inputs={"topic": "the history of coffee"})

print("\n=== Done ===")
print(result)
print("\n-> report.md has been generated. Open it to check the result.")
