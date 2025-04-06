from assistant.core import generate_response
from utils.speech import record_audio, speak_text

if __name__ == "__main__":
    while True:
        user_input = record_audio()
        if user_input in ["exit", "quit", "bye"]:
            speak_text("Goodbye!")
            break
        response = generate_response(user_input)
        speak_text(response)
