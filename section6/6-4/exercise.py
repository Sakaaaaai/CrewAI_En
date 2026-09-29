import os
from dotenv import load_dotenv
from pydantic import BaseModel
from crewai import Agent, Task, Crew, Process, LLM
from crewai.flow.flow import Flow, start, router, listen

load_dotenv()

llm = LLM(model="gemini/gemini-flash-latest")


# Writing Crew (leave this as is)
def build_writing_crew():
    researcher = Agent(role="Researcher", goal="Research the key points of {topic}",
                       backstory="A research expert skilled at spotting the key points.", llm=llm, verbose=False)
    writer = Agent(role="Writer", goal="Write an article following the outline",
                   backstory="A writer who explains things clearly.", llm=llm, verbose=False)
    editor = Agent(role="Editor", goal="Proofread and finalize the article",
                   backstory="A veteran editor with a sharp eye for detail.", llm=llm, verbose=False)
    t1 = Task(description="Research three key points about {topic}.",
              expected_output="3 bullet points", agent=researcher)
    t2 = Task(description="Following the outline below, write a blog article about {topic}.\nOutline:\n{outline}",
              expected_output="Body text (about 300 characters)", agent=writer, context=[t1])
    t3 = Task(description="Proofread the article and finalize it as a Markdown article with a # heading.",
              expected_output="A Markdown article with a # heading", agent=editor, context=[t2])
    return Crew(agents=[researcher, writer, editor], tasks=[t1, t2, t3],
                process=Process.sequential, verbose=False)


class BlogState(BaseModel):
    topic: str = "Focus techniques for remote work"
    outline: str = ""
    article: str = ""


class BlogFlow(Flow[BlogState]):

    @start()
    def create_outline(self):
        self.state.outline = llm.call(
            f"Propose an outline for a blog article titled '{self.state.topic}', as three headings."
        )
        print("=== Outline ===\n", self.state.outline)

    @router(create_outline)
    def approval_gate(self):
        return "approved" if self.state.outline.strip() else "rejected"

    @listen("approved")
    def write_article(self):
        crew = build_writing_crew()
        result = crew.kickoff(inputs={"topic": self.state.topic, "outline": self.state.outline})
        self.state.article = str(result)
        return self.state.article

    # TODO: 1. Create a step that saves the article to a Markdown file after writing
    #   Use @listen(write_article) so it runs once write_article has finished
    #   Write self.state.article out to "article.md" (encoding="utf-8")
    # @listen(write_article)
    # def save_article(self):
    #     with open("article.md", "w", encoding="utf-8") as f:
    #         f.write(self.state.article)
    #     print("-> Saved to article.md")
    #     return "done"

    @listen("rejected")
    def on_rejected(self):
        print("Stopped because the outline was empty.")
        return "stopped"


flow = BlogFlow()
result = flow.kickoff()

print("\n=== Pipeline complete ===")
print(result)
