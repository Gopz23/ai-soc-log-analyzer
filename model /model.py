from sentence_transformers import SentenceTransformer
from transformers import pipeline
import faiss
import numpy as np
from data import load_data

# Load dataset
df = load_data()

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create embeddings
embeddings = model.encode(df['log'].tolist())

# FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# Load LLM
generator = pipeline("text-generation", model="distilgpt2")


def detect_threat(query):
    query_embedding = model.encode([query])
    
    D, I = index.search(query_embedding, k=1)
    
    matched_log = df.iloc[I[0][0]]['log']
    threat_type = df.iloc[I[0][0]]['label']
    
    prompt = f"""
    You are a SOC analyst.
    
    Log: {query}
    Similar Incident: {matched_log}
    Threat Type: {threat_type}
    
    Explain why this is a threat and what actions to take.
    """
    
    response = generator(prompt, max_length=150, num_return_sequences=1)
    
    return threat_type, response[0]['generated_text']
