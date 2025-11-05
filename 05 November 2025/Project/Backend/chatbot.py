def get_chat_response(message: str):
    message = message.lower()

    if any(word in message for word in ["hi", "hello", "hey"]):
        return "👋 Hi there! I'm your ProjectMate assistant. How can I help you today?"
    
    elif "skill" in message:
        return "🧠 Here are some trending skills you could learn: MLOps, React, Data Engineering, and Cloud Fundamentals."

    elif "project" in message or "recommend" in message:
        return "💼 I can recommend internal projects that match your skills. Please tell me your name or skill set!"

    elif "help" in message:
        return "🤝 Sure! I can assist you with finding projects, learning paths, or checking your current skills."

    elif "thank" in message:
        return "You're welcome! Keep learning and growing 🚀"

    elif "bye" in message or "exit" in message:
        return "Goodbye! 👋 Hope you find an awesome project soon."

    else:
        return "Hmm, I'm not sure I understand yet. Try asking about projects, skills, or recommendations!"
