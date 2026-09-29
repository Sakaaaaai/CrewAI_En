import os
from dotenv import load_dotenv
from pydantic import BaseModel
from crewai import LLM
from crewai.flow.flow import Flow, start, router, listen

load_dotenv()

llm = LLM(model="gemini/gemini-flash-latest")


class ReviewState(BaseModel):
    text: str = ""       # input text
    reply: str = ""      # reply text


class SupportFlow(Flow[ReviewState]):

    @start()
    def receive(self):
        # Store the input text in state (fixed for now — you can change it later to experiment)
        self.state.text = "This product is amazing, thank you!"
        print("Received:", self.state.text)

    # --- @router: branches to a different route depending on a judgment result ---
    # Whatever string a @router method returns is picked up by the matching @listen("that string").
    # TODO: 1. Have the LLM judge whether the input text is Japanese or English, and return "japanese" or "english"
    # @router(receive)
    # def detect_language(self):
    #     answer = llm.call(
    #         f"If the following sentence is Japanese, answer only 'japanese'; if it's English, answer only 'english'.\nSentence: {self.state.text}"
    #     )
    #     lang = "japanese" if "japan" in answer.lower() else "english"
    #     print("Detected:", lang)
    #     return lang

    # TODO: 2. "japanese" route: write a reply in Japanese
    # @listen("japanese")
    # def reply_japanese(self):
    #     self.state.reply = llm.call(f"Reply politely in Japanese to this review: {self.state.text}")
    #     return self.state.reply

    # TODO: 3. "english" route: write a reply in English
    # @listen("english")
    # def reply_english(self):
    #     self.state.reply = llm.call(f"Reply politely in English to this review: {self.state.text}")
    #     return self.state.reply


flow = SupportFlow()
result = flow.kickoff()

print("\n=== Reply ===")
print(result)
