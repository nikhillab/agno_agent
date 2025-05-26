import os
from pathlib import Path
import time
from agno.models.ollama import Ollama
from agno.media import Image
from agno.agent import Agent
import yaml


class AgentManager:
    def __init__(self, folder_path="prompts/agents"):
        self.folder_path = folder_path
        self.agents = {}
        self.agent_prompts = {}

    def load_agents(self):
        for filename in os.listdir(self.folder_path):
            if filename.endswith(".yaml") or filename.endswith(".yml"):
                with open(os.path.join(self.folder_path, filename), 'r') as file:
                    config = yaml.safe_load(file)

                    print(f"Loading file: {filename}")

                    agent = Agent(
                        model=Ollama(id="gemma3:4b-it-qat"),
                        agent_id=config.get("agent_id", os.path.splitext(filename)[0]),
                        name=config.get("name", os.path.splitext(filename)[0]),
                        instructions=[config.get("system_message", "")],
                        system_message_role=config.get("system_message_role", "").strip(),
                        markdown=True,
                        debug_mode=True,
                        show_tool_calls=True,
                        goal=config.get("goal", "").strip()
                    )

                    self.agents[agent.agent_id] = agent
                    self.agent_prompts[agent.agent_id] = config.get("main_prompt", "Review the architecture for " + config.get("name"))

    def run_agent(self, agent_name: str, local_image_path: str) -> str:
        print(f"Running agent: {agent_name}")
        agent = self.agents.get(agent_name)
        if not agent:
            return f"Agent {agent_name} not found."

        image_path = Path(local_image_path)
        final_response = ""

        for response in agent.run(
            self.agent_prompts.get(agent_name),
            images=[Image(filepath=image_path)],
            stream=True,
        ):
            final_response += response.content

        return final_response