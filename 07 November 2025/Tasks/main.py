import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv
import json
from datetime import datetime
from pathlib import Path

# Load environment variables
load_dotenv()

app = FastAPI()

# Allow frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

HISTORY_FILE = "qa-history.json"

class Prompt(BaseModel):
    question: str = Field(..., min_length=1, description="Question cannot be empty")

def load_history():
    if Path(HISTORY_FILE).exists():
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_to_history(question, answer):
    history = load_history()
    history.append({
        "timestamp": datetime.now().isoformat(),
        "question": question,
        "answer": answer
    })
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

@app.post("/generate")
async def generate_response(prompt: Prompt):
    if not prompt.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    try:
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise HTTPException(status_code=500, detail="Missing OpenRouter API key")

        # Debug log to confirm key is loaded
        print("Using OpenRouter API key:", api_key[:10] + "...")

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        body = {
            "model": "mistralai/mistral-7b-instruct:free",  # free Mistral model
            "messages": [
                {"role": "user", "content": f"Question: {prompt.question}\n\nAnswer:"}
            ],
            "max_tokens": 500,
            "temperature": 0.7
        }

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=body
        )

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)

        data = response.json()
        answer = data["choices"][0]["message"]["content"]

        save_to_history(prompt.question, answer)

        return {"question": prompt.question, "response": answer}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/history")
async def get_history():
    return load_history()
