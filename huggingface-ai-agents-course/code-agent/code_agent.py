import os
from smolagents import CodeAgent, DuckDuckGoSearchTool, load_tool, tool
import datetime
import requests
import pytz
import yaml
from pathlib import Path

from smolagents import TransformersModel

from Gradio_UI import GradioUI

from tools.final_answer import FinalAnswerTool
from tools.web_search import DuckDuckGoSearchTool
from tools.visit_webpage import VisitWebpageTool

from dotenv import load_dotenv

# read the .env file
load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACE_READ_KEY")
SCRIPT_DIR = Path(__file__).parent

# ToDo: develop tool
@tool
def custom_tool(arg1: str)-> str:
    """A tool for ___________

    Args:
        arg1 (str): ___________

    Returns:
        str: _________
    """
    return "Build something great!"

@tool
def get_current_time_in_timezone(timezone: str) -> str:
    """A tool that returns the current time in a given timezone

    Args:
        timezone (str): A valid timezone as a string (e.g. 'America/Los_Angeles')

    Returns:
        str: Current time in that timezone as a string
    """
    try: 
        tz = pytz.timezone(timezone)
        local_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        return f"The current local time in {timezone} is: {local_time}"
    except Exception as e:
        return f"Error fetching time for timezone: {timezone} - {str(e)}"

def create_model():
    return TransformersModel(
        max_new_tokens=1024,
        model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0', # toggle for different models 
        # model_id='google/gemma-7b-it', # needs to follow {user-answer-user} chain instead of system-user-observation
        # model_id='microsoft/Phi-3-mini-4k-instruct', # needs T4 GPU, and at least a 40 GB RAM machine
        # model_id='HuggingFaceH4/zephyr-7b-beta', # needs T4 GPU, and at least a 40 GB RAM machine
        custom_role_conversions=None,
    )

if __name__ == "__main__":
    final_answer = FinalAnswerTool()
    web_search = DuckDuckGoSearchTool()
    visit_webpage = VisitWebpageTool()

    model = create_model()

    image_generation_tool = load_tool("agents-course/text-to-image", trust_remote_code=True) # add to tools if it fits the use case
    tools = [
        final_answer, 
        get_current_time_in_timezone,
        web_search,
        visit_webpage,
    ]

    with open(SCRIPT_DIR / "agent_config.yaml", 'r') as stream:
        agent_config = yaml.safe_load(stream)
    
    agent = CodeAgent(
        model=model,
        tools=tools,
        max_steps=agent_config.get("max_steps", 6),
        verbosity_level=1,
        planning_interval=None,
        name=None,
        description=None,
        prompt_templates=agent_config["prompt_templates"]
    )


    GradioUI(agent).launch()
