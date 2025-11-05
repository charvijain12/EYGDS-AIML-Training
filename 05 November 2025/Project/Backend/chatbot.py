import random

responses = {
    "greeting": ["Hello! 👋 How can I help you today?", "Hi there! Need help finding a project?"],
    "projects": ["You can check your recommended projects above.", "I can help match you to suitable projects."],
    "upskill": ["Try improving your SQL and Tableau skills!", "Consider learning Flask or NLP for better matches."],
    "default": ["I'm still learning! Could you rephrase that?"]
}

def get_chat_response(message):
    msg = message.lower()
    if "hello" in msg or "hi" in msg:
        return random.choice(responses["greeting"])
    elif "project" in msg:
        return random.choice(responses["projects"])
    elif "improve" in msg or "learn" in msg or "upskill" in msg:
        return random.choice(responses["upskill"])
    else:
        return random.choice(responses["default"])