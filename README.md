🔐 AI-Powered SOC Log Analyzer
🧠 Overview

This project simulates a Security Operations Center (SOC) analyst using AI.

It analyzes security logs, detects threats, and generates explanations using a local LLM.

🚀 Features
Log ingestion
Threat classification
Similarity search using FAISS
AI-generated explanations
🧱 Architecture
Logs → Embeddings → FAISS → LLM → Output
⚙️ Tech Stack
Python
Sentence Transformers
FAISS (Vector DB)
Hugging Face Transformers

▶️ How to Run
git clone https://github.com/your-username/ai-soc-log-analyzer.git
cd ai-soc-log-analyzer

pip install -r requirements.txt

python app.py
🧪 Example
Input:
User tried 10 failed logins in 2 minutes

Output:
Threat: Brute Force
Explanation: ...
