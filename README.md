# ai-soc-log-analyzer
🔐 AI-Powered SOC Log Analyzer with Threat Detection & Explanation
🧠 Description

This project simulates a Security Operations Center (SOC) analyst using artificial intelligence to analyze and interpret security logs. It is designed to automatically detect suspicious activities, classify potential threats, and generate human-readable explanations to assist cybersecurity teams in faster incident response.

The system uses Natural Language Processing (NLP) and vector similarity search to compare incoming logs with known threat patterns. It leverages a lightweight Large Language Model (LLM) to provide contextual explanations and recommended mitigation steps, mimicking the decision-making process of a real SOC analyst.

🚀 Key Capabilities
🔍 Log Analysis: Processes raw security logs as input
⚡ Threat Detection: Identifies suspicious behavior using semantic similarity
🧠 Threat Classification: Categorizes threats (e.g., Brute Force, Malware, Data Exfiltration)
🤖 AI Explanation: Generates detailed explanations using a local LLM
📊 Vector Search: Uses FAISS for fast and efficient similarity matching
🧱 How It Works
Security logs are converted into embeddings using a sentence transformer model
FAISS is used to retrieve the most similar known log pattern
The matched pattern determines the likely threat category
An LLM generates a human-like explanation and suggested actions
⚙️ Technologies Used
Python
Sentence Transformers (all-MiniLM-L6-v2)
FAISS (Vector Database)
Hugging Face Transformers (distilgpt2)
Pandas
🎯 Use Case

This project demonstrates how AI can assist cybersecurity teams by:

Reducing manual effort in log analysis
Speeding up threat identification
Providing explainable insights for decision-making
💡 Future Enhancements
Integration with real-time log streams
Advanced LLMs for better explanations
Web-based dashboard (Streamlit)
Deployment using cloud services (AWS/GCP)
🧪 Example

Input Log:
User tried 10 failed logins in 2 minutes

Output:

Threat Type: Brute Force Attack
Explanation: AI-generated analysis with mitigation steps
