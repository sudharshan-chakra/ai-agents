import re
from react_agent import client, Agent, prompt
from tools import wikipedia, calculate, known_actions

action_re = re.compile("^Action: (\w+): (.*)$")

def query(question, max_turns=5):
    counter = 0
    agent = Agent(system=prompt)
    next_prompt = question

    while counter < max_turns:
        counter += 1

        result = agent(next_prompt)
        print(result)

        actions = [
            action_re.match(action)
            for action in result.split("\n")
            if action_re.match(action)
        ]

        if actions:
            action, action_input = actions[0].groups()
            if action not in known_actions:
                raise Exception(f"Unknown action: {action}: {action_input}")
            print(f" -- running {action}: {action_input}")
            observation = known_actions[action](action_input)
            print(f"Observation: {observation}")
            next_prompt = f"Observation: {observation}"
        else:
            return