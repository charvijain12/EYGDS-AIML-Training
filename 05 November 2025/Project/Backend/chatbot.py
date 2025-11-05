def get_chat_response(message: str) -> str:
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hi there! Need help finding a project that matches your skills?"
    elif "recommend" in message or "project" in message:
        return "Sure! Please tell me your name so I can suggest suitable projects."
    elif "learn" in message or "skill" in message:
        return "Top trending skills: Generative AI, React, Data Engineering, Cloud, and MLOps!"
    elif "thank" in message:
        return "You're welcome! 😊 Keep growing and exploring."
    elif "bye" in message:
        return "Goodbye! Hope you find your perfect project."
    else:
        return "I can help you find internal projects or suggest skills to upskill!"
