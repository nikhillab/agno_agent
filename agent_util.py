from io import BytesIO
from tempfile import NamedTemporaryFile
from PIL import Image



MAX_IMAGE_WIDTH = 500

def resize_image_for_display(image_file):
    """Resize image for display only, returns bytes"""
    if isinstance(image_file, str):
        img = Image.open(image_file)
    else:
        img = Image.open(image_file)
        image_file.seek(0)
    
    aspect_ratio = img.height / img.width
    new_height = int(MAX_IMAGE_WIDTH * aspect_ratio)
    img = img.resize((MAX_IMAGE_WIDTH, new_height), Image.Resampling.LANCZOS)
    
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()

def save_uploaded_file(uploaded_file):
    with NamedTemporaryFile(dir='./input', suffix='.jpg', delete=False) as f:
        f.write(uploaded_file.getbuffer())
        return f.name



def get_agent_from_select_option(select_option: str) -> str:
    map={
        "Architectural Components":"component_extractor_agent",
        "Connectivity and Integration":"connection_extractor_agent",
        "Security and Compliance Controls":"security_pillar_agent",
        "Cost Optimization":"cost_optimization_agent",
        "Performance and Scalability":"performance_efficiency_agent",
        "Reliability and Fault Tolerance":"reliability_agent",
        "Operational Efficiency and Manageability":"operational_excellence_agent",
    }
    return map[select_option]