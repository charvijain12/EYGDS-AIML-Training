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
            op, nums = data.split(":")
            numbers = list(map(float, nums.split(",")))

            if len(numbers) < 2:
                return {"error": "Need at least two numbers."}

            operations = {
                "add": lambda nums: sum(nums),
                "subtract": lambda nums: numbers[0] - sum(numbers[1:]),
                "multiply": lambda nums: eval("*".join(map(str, nums))),
                "divide": lambda nums: divide_numbers(nums)
            }

            if op not in operations:
                return {"error": f"Invalid operation '{op}'."}

            result = operations[op](numbers)
            return {"result": result}

        except Exception as e:
            return {"error": f"Error processing math operation: {e}"}

    elif action == "date":
        return {"result": str(date.today())}

    else:
        return {"error": "Invalid action. Use 'reverse', 'math', or 'date'."}


def divide_numbers(nums):
    result = nums[0]
    for n in nums[1:]:
        if n == 0:
            raise ValueError("Division by zero not allowed.")
        result /= n
    return result