from transformers import pipeline

# Load HuggingFace model (distilGPT2 for demo)
chatbot = pipeline("text-generation", model="distilgpt2")

def query_model(prompt: str) -> str:
    response = chatbot(prompt, max_length=100, do_sample=True)[0]['generated_text']
    return response[len(prompt):].strip()
