from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
from openai import OpenAI
from dotenv import load_dotenv
import logging
import time
import os

# -----------------------------------
# Load environment variables from .env
# -----------------------------------
load_dotenv()

app = FastAPI()

# -----------------------------------
# Setup logging and OpenAI client
# -----------------------------------
logging.basicConfig(level=logging.INFO)

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables or .env file")

client = OpenAI(api_key=openai_api_key)

# -----------------------------------
# Model class (AI model within FastAPI)
# -----------------------------------
class OpenAIModel:
    def __init__(self, model_name="gpt-4.1-mini"):
        self.model_name = model_name

    def predict(self, text: str):
        response = client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You are a helpful text analysis assistant."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content.strip()

ai_model = OpenAIModel()

# -----------------------------------
# Pydantic schema
# -----------------------------------
class Query(BaseModel):
    action: str
    data: str

# -----------------------------------
# Middleware for logging
# -----------------------------------
@app.middleware("http")
async def log_requests(request, call_next):
    start = time.time()
    logging.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    duration = round(time.time() - start, 3)
    logging.info(f"Completed in {duration}s with status {response.status_code}")
    return response

# -----------------------------------
# API endpoint
# -----------------------------------
@app.post("/process")
def process_query(query: Query):
    action = query.action.lower()
    data = query.data.strip()

    if action == "reverse":
        return {"result": data[::-1]}

    elif action == "math":
        try:
            op, nums = data.split(":")
            numbers = list(map(float, nums.split(",")))
            if len(numbers) < 2:
                return {"error": "Need at least two numbers."}

            if op == "add":
                result = sum(numbers)
            elif op == "subtract":
                result = numbers[0] - sum(numbers[1:])
            elif op == "multiply":
                result = 1
                for n in numbers:
                    result *= n
            elif op == "divide":
                result = numbers[0]
                for n in numbers[1:]:
                    if n == 0:
                        raise ValueError("Division by zero not allowed.")
                    result /= n
            else:
                return {"error": f"Invalid operation '{op}'."}

            return {"result": result}

        except Exception as e:
            return {"error": f"Error processing math operation: {e}"}

    elif action == "date":
        return {"result": str(date.today())}

    elif action == "ai":
        try:
            prediction = ai_model.predict(data)
            return {"result": prediction}
        except Exception as e:
            return {"error": f"AI model error: {e}"}

    else:
        return {"error": "Invalid action. Use 'reverse', 'math', 'date', or 'ai'."}