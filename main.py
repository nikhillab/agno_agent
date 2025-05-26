from io import BytesIO
import os
from pathlib import Path
from agno.media import Image
from agno.models.ollama import Ollama
from agno.agent import Agent
from agno.models.google import Gemini

from util import resize_image_for_display







def main():


    # resized_image = resize_image_for_display("aws.jpg",)
    # print(resized_image)

    agent = Agent(
    model=Ollama(id="gemma3:4b-it-qat"),
    agent_id="connection_extractor_agent",
    name="Connection Extractor",
    system_message_role="You are an expert cloud network analyst",
    instructions=[
        "Your sole task is to read a cloud architecture description (diagram JSON or text) and identify every logical connection between components.Present your findings in a concise table without any additional commentary."

    ],
    markdown=True,
    debug_mode=True,
    show_tool_calls=False,
    goal="Extract all directed relationships among services/components in the input and output them as a markdown table listing Source, Target, Relationship, and any key Details.",
    )


    image_path = Path(__file__).parent.joinpath("aws1.png")

    final_responce=""
    
    for res in agent.run("""
            Extract and describe the network connections and integrations between components. Include data flow and protocol details where applicable.  
            """,
            images=[Image(filepath=image_path)],
            stream=True,
            ):
        final_responce += res.content
    print("RESULT: ")
    print(final_responce)

# import yaml

# from agents import component_extractor_agent 

# with open('prompts/prompts.yaml', 'r') as file:
#     prompts = yaml.safe_load(file)
#     file.close()

# image_path = Path(__file__).parent.joinpath("aws.jpg")

# component_extractor_agent.print_response(prompts['component_extractor_agent'],
#     images=[Image(filepath=image_path)],
#     stream=True,
#     )

# agent = Agent(
#     model=Gemini(id="gemini-2.5-flash-preview-05-20",api_key=""),
#     agent_id="image-to-text",
#     name="Image to Text Agent",
#     system_message_role="You are an expert cloud network analyst.",
#     system_message="""
#         Your sole task is to read a cloud architecture description (diagram JSON or text) and 
#         identify every logical connection between components. Present your findings in a concise 
#         table without any additional commentary.        
#     """,
#     markdown=True,
#     debug_mode=True,
#     show_tool_calls=False,
#     goal="Extract all directed relationships among services/components in the input and output them as a markdown table listing Source, Target, Relationship, and any key Details.",
    
# )


# image_path = Path(__file__).parent.joinpath("aws.jpg")


# agent.print_response("""
#     You will be given a cloud architecture description (either JSON or diagram).  
#     Your task is to extract **every** logical connection or data flow between components.  

#         1. Read the input carefully and identify each edge (arrow, link, or reference).
#         2. For each connection, determine:
#             - **Source**: Name of the originating component or service  
#             - **Target**: Name of the receiving component or service  
#             - **Relationship**: One of (invokes, connects_to, routes_through, hosts, monitored_by, secured_by, triggers, contains, etc.)  
#             - **Details**: (optional) protocol, port, direction, or confidence level  

#         3. Output **only** a markdown table with these headers and one row per connection. No extra text.
#         """,
#     images=[Image(filepath=image_path)],
#     stream=True,
#     )

if __name__ == "__main__":
    main()

    