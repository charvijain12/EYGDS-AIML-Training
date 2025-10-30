import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

# ------------------------------------------------------------
# 1. Load Environment Variables
# ------------------------------------------------------------
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

if not api_key:
    raise ValueError("Missing OPENROUTER_API_KEY in .env file")

# ------------------------------------------------------------
# 2. Initialize Model and Memory
# ------------------------------------------------------------
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    temperature=0.4,
    max_tokens=256,
    api_key=api_key,
    base_url=base_url,
)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
notes = []  # store notes in memory

# ------------------------------------------------------------
# 3. Tool Functions
# ------------------------------------------------------------
def summarize_text(text: str) -> str:
    """Summarize long text."""
    prompt = f"Summarize the following text in one sentence: {text}"
    return llm.invoke(prompt).content.strip()

def analyze_sentiment(text: str) -> str:
    """Detect emotional tone."""
    prompt = f"Analyze the sentiment of this text as positive, neutral, or negative: {text}"
    return llm.invoke(prompt).content.strip()

def improve_text(text: str) -> str:
    """Rewrite text to be clearer and more professional."""
    prompt = f"Rewrite this text to make it clearer and more professional: {text}"
    return llm.invoke(prompt).content.strip()

def classify_priority(task: str) -> str:
    """Categorize task as high, medium, or low priority."""
    high_keywords = ["urgent", "today", "tonight", "immediately", "asap", "deadline", "submit"]
    low_keywords = ["buy", "snack", "clean", "organize", "casual"]

    task_lower = task.lower()
    if any(k in task_lower for k in high_keywords):
        priority = "HIGH"
    elif any(k in task_lower for k in low_keywords):
        priority = "LOW"
    else:
        priority = "MEDIUM"

    return f'Task "{task}" marked as {priority} priority.'

def add_note(note_text: str) -> str:
    """Store personal note."""
    notes.append(note_text)
    return f'Noted: "{note_text}".'

def get_all_notes() -> str:
    """Retrieve all notes."""
    if not notes:
        return "You currently have no saved notes."
    return "You currently have " + str(len(notes)) + " notes: " + "; ".join(notes)

# ------------------------------------------------------------
# 4. Main Conversational Loop
# ------------------------------------------------------------
print("\n=== AI Productivity Assistant ===")
print("Commands: summarize / analyze / note / get notes / improve / priority / exit\n")

while True:
    user_input = input("You: ").strip()
    if not user_input:
        continue
    if user_input.lower() == "exit":
        print("Agent: Goodbye")
        break

    # Summarizer
    if user_input.lower().startswith("summarize"):
        text = user_input.replace("summarize", "", 1).strip()
        if not text:
            print("Agent: Please provide text to summarize.")
            continue
        summary = summarize_text(text)
        print("Agent:", summary)
        memory.save_context({"input": user_input}, {"output": summary})
        continue

    # Sentiment Analyzer
    if user_input.lower().startswith("analyze"):
        text = user_input.replace("analyze", "", 1).strip()
        if not text:
            print("Agent: Please provide text to analyze.")
            continue
        sentiment = analyze_sentiment(text)
        print("Agent:", sentiment)
        memory.save_context({"input": user_input}, {"output": sentiment})
        continue

    # NoteKeeper
    if user_input.lower().startswith("note"):
        note_text = user_input.replace("note", "", 1).strip()
        if not note_text:
            print("Agent: Please provide note content.")
            continue
        result = add_note(note_text)
        print("Agent:", result)
        memory.save_context({"input": user_input}, {"output": result})
        continue

    if user_input.lower().startswith("get notes"):
        result = get_all_notes()
        print("Agent:", result)
        memory.save_context({"input": user_input}, {"output": result})
        continue

    # Text Improver
    if user_input.lower().startswith("improve"):
        text = user_input.replace("improve", "", 1).strip()
        if not text:
            print("Agent: Please provide text to improve.")
            continue
        improved = improve_text(text)
        print("Agent:", improved)
        memory.save_context({"input": user_input}, {"output": improved})
        continue

    # Task Priority Classifier
    if user_input.lower().startswith("priority"):
        task = user_input.replace("priority", "", 1).strip()
        if not task:
            print("Agent: Please describe the task.")
            continue
        result = classify_priority(task)
        print("Agent:", result)
        memory.save_context({"input": user_input}, {"output": result})
        continue

    # Default LLM response
    response = llm.invoke(user_input)
    print("Agent:", response.content)
    memory.save_context({"input": user_input}, {"output": response.content})
