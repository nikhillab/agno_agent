import streamlit as st

from agents import AgentManager
import agent_util


 

def process_agent(agent_select: str, provider: str,image_path: str) -> str:
    with st.spinner(f"🔍 Running {agent_select} analysis... Please wait!"):
        agent_name=agent_util.get_agent_from_select_option(agent_select)
        return st.session_state.agent_manager.run_agent(agent_name=agent_name,local_image_path=image_path)
        # return "demo test"

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #023e8a;
        color: #333333;
    }
    .main {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    h1 {
        color: #4a90e2;
        font-size: 3em;
    }
    h2 {
        color: #333333;
    }
    .stButton>button {
        background-color: #4a90e2;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 1em;
    }
    .stButton>button:hover {
        background-color: #3c7dc9;
    }
    .css-1aumxhk { /* Multiselect styling */
        background-color: #ffffff;
        border: 1px solid #4a90e2;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "provider" not in st.session_state:
    st.session_state.provider = "AWS"

if "custom_provider" not in st.session_state:
    st.session_state.custom_provider = ""

if "selected_agents" not in st.session_state:
    st.session_state.selected_agents = []

if "run_evaluation" not in st.session_state:
    st.session_state.run_evaluation = False

if "uploaded_image" not in st.session_state:
    st.session_state.uploaded_image = None

if "input_json" not in st.session_state:
    st.session_state.input_json = ""

if "agent_manager" not in st.session_state:
    st.session_state.agent_manager = AgentManager()
    st.session_state.agent_manager.load_agents()

def run_evaluation():
    print("run_evaluation")
    st.session_state.run_evaluation = True

def reset_run_evaluation():
    print("reset_run_evaluation")
    st.session_state.run_evaluation = False
    st.session_state.selected_agents = []

# Reset function
def reset_state():
    print("reset_state")
    st.session_state.run_evaluation = False
    st.session_state.selected_agents = []
    st.session_state.provider = "AWS"
    st.session_state.custom_provider = ""
    st.session_state.uploaded_image = None
    st.session_state.input_json = ""

# App Title and Header
st.markdown("<h1>Cloud Architecture Reviewer 🚀</h1>", unsafe_allow_html=True)
st.markdown("<h3>Uncover Insights & Optimize Your Cloud Design</h3>", unsafe_allow_html=True)
st.markdown("""
                <p>Welcome to Cloud Architecture Reviewer!  
                Easily analyze your cloud infrastructure and gain actionable insights.  
                Whether you're using AWS, Azure, GCP, or a mix of providers – we’ve got you covered.</p>
            """,
             unsafe_allow_html=True)


# Cloud Provider Selection
st.session_state.provider = st.selectbox(
    "🌐 Choose Your Cloud Provider",
    ["AWS", "Azure", "GCP", "Mixed", "Others"],
    index=["AWS", "Azure", "GCP", "Mixed", "Others"].index(st.session_state.provider),
    on_change = reset_run_evaluation
)

if st.session_state.provider in ["Mixed", "Others"]:
    st.session_state.custom_provider = st.text_input(
        "📝🌟 Specify Your Cloud Provider (if Mixed or Others)",
        value=st.session_state.custom_provider
    )

# Agent Selection
st.session_state.selected_agents = st.multiselect(
    "🛠️ Select Review Categories",
    [
        "Architectural Components",
        "Connectivity and Integration",
        "Cloud Best Practices",
        "Security and Compliance Controls",
        "Cost Optimization",
        "Performance and Scalability",
        "Reliability and Fault Tolerance",
        "Operational Efficiency and Manageability"
    ],
    default=st.session_state.selected_agents,
    on_change = reset_run_evaluation
)

st.markdown("---")

# Tabs for Image Upload and JSON Input
tabs = st.tabs(["📸 Upload Your Architecture Diagram", "📄 Paste or Write Your JSON Configuration"])
with tabs[0]:
    st.session_state.uploaded_image = st.file_uploader("Upload an Image (e.g., architecture diagram)", type=["png", "jpg", "jpeg"])

with tabs[1]:
    st.session_state.input_json = st.text_area("Input JSON Content", value=st.session_state.input_json, height=200)

st.markdown("---")

# Buttons
col1, col2 = st.columns([1, 1])
with col1:
    st.button("🚀 Launch Architecture Review",on_click=run_evaluation)
        
with col2:
    st.button("🔄 Reset All Fields",on_click=reset_state)
        



# Display Results
if st.session_state.run_evaluation:
    if st.session_state.input_json:
        st.markdown("**Input JSON:**")
        try:
            eval(st.session_state.input_json)
        except:
            st.warning("⚠️ Oops! The provided JSON is not valid. Please check and try again.")

    if st.session_state.uploaded_image:
        resized_image = agent_util.resize_image_for_display(st.session_state.uploaded_image)
        st.image(resized_image, caption="Your Uploaded Architecture Diagram", use_container_width=False, width=agent_util.MAX_IMAGE_WIDTH)

    if st.session_state.selected_agents:
        st.info(body="""
                    🎉 Explore the tabs below! To get detailed insights for each selected category.  
            """)
        
        temp_path = agent_util.save_uploaded_file(st.session_state.uploaded_image)
        print("Temp Path:",temp_path)

        result_tabs = st.tabs(st.session_state.selected_agents)
        for tab, agent in zip(result_tabs, st.session_state.selected_agents):
            with tab:
                result_text = process_agent(agent,st.session_state.provider,temp_path)
                st.markdown(f"### 🔍 {agent} Agent Result ")
                st.markdown(f"✅ Evaluation completed successfully for **{agent}**.\n")
                st.markdown(result_text)
    else:
        st.warning("⚠️ Please select at least one review category to begin evaluation.")
else:
    st.info("💡 Click **Launch Architecture Review 🚀** to analyze your architecture and view the results.")