from .ai_model import query_model

def generate_response(user_input: str) -> str:
    if not user_input:
        return "Sorry, I didn't catch that. Could you repeat?"
    return query_model(user_input)
