import os
import time
from agno.models.ollama import Ollama
from agno.agent import Agent
import yaml

# Path to folder containing YAML files
FOLDER_PATH = "prompts/agents"

# Dictionary to store agent instances
agents = {}

def load_agents():
    # Loop through each YAML file and create Agent instance
    for filename in os.listdir(FOLDER_PATH):
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            with open(os.path.join(FOLDER_PATH, filename), 'r') as file:
                config = yaml.safe_load(file)

                # Create Agent instance
                agent = Agent(
                    model=Ollama(id="gemma3:4b-it-qat"),
                    agent_id=config.get("agent_id", os.path.splitext(filename)[0]),
                    name=config.get("name", os.path.splitext(filename)[0]),
                    instructions=[config.get("system_message_role", "")],
                    system_message=config.get("system_message", "").strip(),
                    markdown=True,
                    debug_mode=True,
                    show_tool_calls=True,
                    goal=config.get("goal", "").strip()
                )

                # Add to dictionary
                agents[agent.agent_id] = agent
    print(agents.keys())



def run_agent(agent_name: str):
    print("running agent",agent_name)

    agent = agents.get(agent_name)
    agent.run()
    time.sleep(15)