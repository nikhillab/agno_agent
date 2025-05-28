
# 🌥️ Cloud Architecture Review App  

This **Streamlit-based web application** allows users to **analyze and review cloud architectures** (AWS, Azure, GCP, or hybrid) by:  
- Uploading **image diagrams** or **JSON configurations**.  
- Running **AI-powered agents** to extract components, connections, best practices, security gaps, and more.  
- Presenting results in a **tabbed, interactive format**.  

---

## 🚀 Features  
- **Upload Architecture**: Supports images or JSON files.  
- **Multi-Cloud Support**: AWS, Azure, GCP, Mixed, Others.  
- **Agent Evaluations**:
  - 🔍 Components
  - 🔗 Connections
  - ✅ Best Practices
  - 🔒 Security
  - 💰 Cost Optimization
  - 🚀 Performance
  - 🌐 Reliability
  - 🛠️ Operational Excellence  
- **Dynamic Tabbed Results**: View different analysis outputs in separate tabs.  
- **Loading Feedback**: Spinners/animations while agents are running.  
- **Reset Controls**: Reset uploaded files or evaluation states dynamically.  

---

## 🛠️ Technologies  
- **Python 3.x**  
- **Streamlit** for frontend interactivity  
- **YAML configurations** for dynamic agent creation  
- **Custom Agent Classes** (using `Ollama`, `Image`, and `Agent` modules)  
- **Markdown Rendering** of results  

---

## 📂 Project Structure  
```
📦 your_project/
├── prompts/
│   └── agents/
│       ├── best_practices.yaml
│       ├── component_extractor.yaml
│       ├── ...
├── main_app.py
├── requirements.txt
├── README.md
└── config.json (optional)
```

---

## 🏃 How to Run
1️⃣ **Install Requirements**  
```bash
pip install -r requirements.txt
```

2️⃣ **Start Streamlit App**  
```bash
streamlit run main_app.py
```

3️⃣ **Open in Browser**  
Visit \`http://localhost:8501\`  

---

## 📥 Upload Options  
- **Image Upload**: Upload `.png`, `.jpg`, or `.jpeg` diagrams.  
- **JSON Upload**: Upload JSON configuration files (e.g., Terraform, CloudFormation).  

---

## 📢 TODO
- [ ] Support YAML/JSON uploads for provider configurations.  
- [ ] Add authentication for multi-user scenarios.  
- [ ] Improve UI styling and branding.  

---

## 🤝 Contributing
Pull requests welcome! Fork the repo, make your changes, and submit a PR.

---

## 📝 License
[MIT License](LICENSE)
