from assistant.core import generate_response
from utils.speech import record_audio, engine_speak

def handle_user_input(mode="voice", user_text=None):
    if mode == "voice":
        voice_data = record_audio("Listening...")
        response = generate_response(voice_data)
        engine_speak(response)
        return {"user": voice_data, "assistant": response}
    else:
        response = generate_response(user_text)
        return {"assistant": response}
