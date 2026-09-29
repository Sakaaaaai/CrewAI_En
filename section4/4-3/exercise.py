import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai.project import CrewBase, agent, task, crew

load_dotenv()


# --- @CrewBase: CrewAI's standard style for bundling a Crew into a class ---
# It automatically loads config/agents.yaml and config/tasks.yaml, and lets you
# define agents and tasks via method names. This is the form you'll see most in
# real-world projects and the official documentation.
@CrewBase
class ContentCrew:
    """Article-writing crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def __init__(self):
        self.llm = LLM(model="gemini/gemini-flash-latest")

    # TODO: 1. Define researcher with a method decorated with @agent
    #   self.agents_config["researcher"] holds the content from the YAML
    # @agent
    # def researcher(self) -> Agent:
    #     return Agent(config=self.agents_config["researcher"], llm=self.llm, verbose=True)

    # TODO: 2. Define writer with @agent
    # @agent
    # def writer(self) -> Agent:
    #     return Agent(config=self.agents_config["writer"], llm=self.llm, verbose=True)

    # TODO: 3. Define research_task with @task
    #   The agent: researcher entry in the YAML is automatically linked to the researcher defined above
    # @task
    # def research_task(self) -> Task:
    #     return Task(config=self.tasks_config["research_task"])

    # TODO: 4. Define write_task with @task (receive the previous step's result via context)
    # @task
    # def write_task(self) -> Task:
    #     return Task(config=self.tasks_config["write_task"], context=[self.research_task()])

    # TODO: 5. Assemble the Crew with @crew
    #   self.agents and self.tasks are automatically populated with everything defined via @agent/@task
    # @crew
    # def crew(self) -> Crew:
    #     return Crew(
    #         agents=self.agents,
    #         tasks=self.tasks,
    #         process=Process.sequential,
    #         verbose=True,
    #     )


result = ContentCrew().crew().kickoff(inputs={"topic": "space elevators"})

print("\n=== Article ===")
print(result)
