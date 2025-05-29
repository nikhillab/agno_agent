from tempfile import NamedTemporaryFile
import agent_util
from agents import AgentManager


def main():
    image_path='aws.jpg'
    agent_manager = AgentManager()
    agent_manager.load_agents()
    agents_names = [
        "Architectural Components",
        "Connectivity and Integration",
        "Security and Compliance Controls",
        "Cost Optimization",
        "Performance and Scalability",
        "Reliability and Fault Tolerance",
        "Operational Efficiency and Manageability"
    ]
    
    for agent_select in agents_names:
        agent_name=agent_util.get_agent_from_select_option(agent_select)
        responce = agent_manager.run_agent(agent_name=agent_name,local_image_path=image_path)
        with NamedTemporaryFile(dir='./output', suffix='.md', delete=False, prefix=agent_name, mode='wb') as f:
            f.write(responce.encode('utf-8'))


if __name__ == "__main__":
    main()

    