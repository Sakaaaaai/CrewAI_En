import os
from dotenv import load_dotenv
from pydantic import BaseModel
from crewai import LLM
from crewai.flow.flow import Flow, start, router, listen

load_dotenv()

llm = LLM(model="gemini/gemini-flash-latest")


# --- Capstone exercise: building the "skeleton" of a blog-article-writing pipeline ---
# Flow of the finished version:
#   Topic input → generate an outline → approval check (mock) → [approved] write / [rejected] stop
# This exercise focuses on state design and "placing" @start / @router / @listen (the writing itself comes in 6-3).

# TODO: 1. Design the state shared across the whole pipeline
#   topic: str    … the topic
#   outline: str  … the generated outline
#   article: str  … the final article (filled in in 6-3)
# class BlogState(BaseModel):
#     topic: str = "Focus techniques for remote work"
#     outline: str = ""
#     article: str = ""


# class BlogFlow(Flow[BlogState]):
class BlogFlow(Flow):

    # TODO: 2. Generate the outline in @start()
    #   Ask the LLM for "an outline for a blog article about {topic}, as three headings" and save it to self.state.outline
    # @start()
    # def create_outline(self):
    #     self.state.outline = llm.call(
    #         f"Propose an outline for a blog article titled '{self.state.topic}', as three headings."
    #     )
    #     print("=== Outline ===\n", self.state.outline)

    # TODO: 3. Build an approval check (mock) with @router
    #   In a real system a human would approve it, but here we treat it as "approved if the outline isn't empty"
    #   Return "approved" or "rejected"
    # @router(create_outline)
    # def approval_gate(self):
    #     return "approved" if self.state.outline.strip() else "rejected"

    # TODO: 4. @listen("approved") … the approved case (replaced with the writing Crew in 6-3; a placeholder message for now)
    # @listen("approved")
    # def on_approved(self):
    #     print("Approved. Proceeding to writing (implemented in 6-3).")
    #     self.state.article = "(the article will go here)"
    #     return self.state.article

    # TODO: 5. @listen("rejected") … the rejected case
    # @listen("rejected")
    # def on_rejected(self):
    #     print("Stopped because the outline was empty.")
    #     return "stopped"
    pass


flow = BlogFlow()
result = flow.kickoff()

print("\n=== Result ===")
print(result)
