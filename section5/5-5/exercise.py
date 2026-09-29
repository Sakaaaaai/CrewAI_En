import os
from dotenv import load_dotenv
from pydantic import BaseModel
from crewai import Agent, Task, Crew, Process, LLM
from crewai.flow.flow import Flow, start, listen

load_dotenv()

llm = LLM(model="gemini/gemini-flash-latest")


# Function that builds the writing Crew (leave this as is. The 2-agent Crew from section 2)
def build_writing_crew():
    researcher = Agent(role="Researcher", goal="Research the key points of {topic}",
                       backstory="A research expert skilled at spotting the key points.", llm=llm, verbose=False)
    writer = Agent(role="Writer", goal="Write an introductory article based on the key points",
                   backstory="A writer who explains things clearly.", llm=llm, verbose=False)
    t1 = Task(description="Research three key points about {topic}.",
              expected_output="3 bullet points", agent=researcher)
    t2 = Task(description="Based on the key points, write an introductory article of about 150 characters.",
              expected_output="An introductory article of about 150 characters", agent=writer, context=[t1])
    return Crew(agents=[researcher, writer], tasks=[t1, t2],
                process=Process.sequential, verbose=False)


class ArticleState(BaseModel):
    topic: str = ""
    article: str = ""


class ArticleFlow(Flow[ArticleState]):

    @start()
    def set_topic(self):
        # The Flow directs traffic for the whole pipeline: first, decide on the topic
        self.state.topic = "space food"
        print("Topic:", self.state.topic)

    # TODO: 1. Using @listen(set_topic), create a step that calls the writing Crew
    #   - Build the Crew with build_writing_crew()
    #   - Run it with crew.kickoff(inputs={"topic": self.state.topic})
    #   - Save the result as a string in self.state.article (str(result))
    # @listen(set_topic)
    # def run_crew(self):
    #     crew = build_writing_crew()
    #     result = crew.kickoff(inputs={"topic": self.state.topic})
    #     self.state.article = str(result)
    #     return self.state.article


flow = ArticleFlow()
result = flow.kickoff()

print("\n=== Finished article ===")
print(result)
