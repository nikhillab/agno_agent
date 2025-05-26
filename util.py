from PIL import Image



MAX_IMAGE_WIDTH = 500
FOLDER = "output/"

"""Resize image"""
def resize_image_for_display(image_file: str) -> str:
    final_path = FOLDER+image_file
    
    if isinstance(image_file, str):
        img = Image.open(image_file)
    else:
        img = Image.open(image_file)
        image_file.seek(0)
    
    aspect_ratio = img.height / img.width
    new_height = int(MAX_IMAGE_WIDTH * aspect_ratio)
    img = img.resize((MAX_IMAGE_WIDTH, new_height), Image.Resampling.LANCZOS)

    img.save(final_path)

    return final_path


def get_agent_to_select_map() -> dict[str, str]:
    map={
        "Architectural Components":"component_extractor_agent",
        "Connectivity and Integration":"connection_extractor_agent",
        "Cloud Best Practices":"best_practices_agent",
        "Security and Compliance Controls":"security_pillar_agent",
        "Cost Optimization":"cost_optimization_agent",
        "Performance and Scalability":"performance_efficiency_agent",
        "Reliability and Fault Tolerance":"reliability_agent",
        "Operational Efficiency and Manageability":"operational_excellence_agent",
    }
    return map