import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

# read the .env file
load_dotenv()

HF_TOKEN = os.getenv("HUGGINGFACE_READ_KEY")
SYSTEM_PROMPT = """Answer the following questions as best you can. You have access to the following tools:

get_weather: Get the current weather in a given location

The way you use the tools is by specifying a json blob.
Specifically, this json should have an `action` key (with the name of the tool to use) and an `action_input` key (with the input to the tool going here).

The only values that should be in the "action" field are:
get_weather: Get the current weather in a given location, args: {"location": {"type": "string"}}
example use :

{{
  "action": "get_weather",
  "action_input": {"location": "New York"}
}}


ALWAYS use the following format:

Question: the input question you must answer
Thought: you should always think about one action to take. Only one action at a time in this format:
Action:

$JSON_BLOB (inside markdown cell)

Observation: the result of the action. This Observation is unique, complete, and the source of truth.
(this Thought/Action/Observation can repeat N times, you should take several steps when needed. The $JSON_BLOB must be formatted as markdown and only use a SINGLE action at a time.)

You must always end your output with the following format:

Thought: I now know the final answer
Final Answer: the final answer to the original input question

Now begin! Reminder to ALWAYS use the exact characters `Final Answer:` when you provide a definitive answer. """

def chat_agent(query:str):

    # still hallucinates, we have to include an actual weather API call to get
    # the precise answer
    
    messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": query},
        ]

    client = InferenceClient(model="meta-llama/Llama-4-Scout-17B-16E-Instruct", token=HF_TOKEN)

    output = client.chat.completions.create(
        messages=messages,
        stream=False,
        max_tokens=1024,
    )

    print(output.choices[0].message.content)

if __name__ == "__main__":
    while True:
        query = input("Question (q to quit): ")
        if query.lower() == "q":
            break
        chat_agent(query)
