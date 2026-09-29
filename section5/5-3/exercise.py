import os
from dotenv import load_dotenv
from pydantic import BaseModel
from crewai.flow.flow import Flow, start, listen

load_dotenv()


# --- state: "state" shared across the entire Flow ---
# If you define the shape of the state as a typed Pydantic model,
# any step can read and write it through self.state.

# TODO: 1. Define the shape of the state as a Pydantic model
#   counter: int = 0          … a counter
#   history: list[str] = []   … a history of what ran
# class CounterState(BaseModel):
#     counter: int = 0
#     history: list[str] = []


# TODO: 2. Create the Flow with the type specified, like Flow[CounterState]
# class CounterFlow(Flow[CounterState]):
class CounterFlow(Flow):

    @start()
    def step_one(self):
        # TODO: 3. Increment self.state.counter by 1 and append "step_one" to history
        # self.state.counter += 1
        # self.state.history.append("step_one")
        print("step_one ran")

    @listen(step_one)
    def step_two(self):
        # TODO: 4. Increment counter by 1 again and append "step_two" to history
        # self.state.counter += 1
        # self.state.history.append("step_two")
        print("step_two ran")


flow = CounterFlow()
flow.kickoff()

print("\n=== Final state ===")
print("counter:", flow.state.counter)
print("history:", flow.state.history)
