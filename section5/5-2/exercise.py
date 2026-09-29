import os
from dotenv import load_dotenv
from crewai.flow.flow import Flow, start, listen

load_dotenv()


# --- Flow: a mechanism for writing processing as a "flow of steps" ---
# @start() … the step that runs first
# @listen(previous step) … the step that runs once the previous step finishes
#   The previous step's "return value" is passed in as the argument to the next step.

class GreetingFlow(Flow):

    # TODO: 1. Create the first step, decorated with @start()
    #   It should return a name (e.g. "Taro")
    # @start()
    # def generate_name(self):
    #     print("Step 1: deciding on a name")
    #     return "Taro"

    # TODO: 2. Create the next step with @listen(generate_name)
    #   It should receive the previous step's return value (the name), build a greeting, and return it
    # @listen(generate_name)
    # def make_greeting(self, name):
    #     print("Step 2: building the greeting")
    #     return f"Hello, {name}!"
    pass


flow = GreetingFlow()
result = flow.kickoff()

print("\n=== Final result ===")
print(result)   # the return value of the last step is printed
