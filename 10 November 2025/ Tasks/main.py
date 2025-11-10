from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
import operator

app = FastAPI()

class Query(BaseModel):
    action: str
    data: str

@app.post("/process")
def process_query(query: Query):
    action = query.action.lower()
    data = query.data.strip()

    if action == "reverse":
        return {"result": data[::-1]}

    elif action == "math":
        try:
            # Safe evaluation of math expression
            result = eval(data, {"__builtins__": None}, {
                "abs": abs, "round": round, "pow": pow, 
                "max": max, "min": min
            })
            return {"result": result}
        except Exception as e:
            return {"error": f"Invalid math expression: {e}"}

    elif action == "date":
        return {"result": str(date.today())}

    else:
        return {"error": "Invalid action. Use 'reverse', 'math', or 'date'."}