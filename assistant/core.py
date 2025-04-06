def generate_response(user_input):
    if "name" in user_input:
        return "My name is Booddi, your voice assistant."
    elif "time" in user_input:
        from time import ctime
        return f"The current time is {ctime()}"
    else:
        return "I'm still learning. Try asking something else."
