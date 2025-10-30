# ============================================================
# Memory-Tools.py — Conversational Mistral Agent (fully working)
# ============================================================

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory


# ------------------------------------------------------------
# 1. Load environment variables
# ------------------------------------------------------------
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env file")


# ------------------------------------------------------------
# 2. Initialize the Mistral model via OpenRouter
# ------------------------------------------------------------
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    temperature=0.4,
    max_tokens=256,
    api_key=api_key,
    base_url=base_url,
)


# ------------------------------------------------------------
# 3. Define helper tools
# ------------------------------------------------------------
def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b


def greet(name: str) -> str:
    """Return a friendly greeting."""
    name = name.strip().replace('"', "").replace("'", "")
    return f"Hello {name}, welcome to the AI Agent demo!"


# ------------------------------------------------------------
# 4. Initialize memory
# ------------------------------------------------------------
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)


# ------------------------------------------------------------
# 5. Conversational loop
# ------------------------------------------------------------
print("\n=== Start chatting with your Agent ===")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        print("\nConversation ended.")
        break

    # Handle Multiply command
    if user_input.lower().startswith("multiply"):
        try:
            parts = user_input.split()
            a, b = int(parts[1]), int(parts[2])
            result = multiply(a, b)
            print("Agent:", result)
            memory.save_context({"input": user_input}, {"output": str(result)})
            continue
        except Exception:
            print("Agent: Please use 'Multiply a b' format.")
            continue

    # Handle Greet command
    if user_input.lower().startswith("greet"):
        try:
            name = " ".join(user_input.split()[1:]).strip()
            if not name:
                print("Agent: Please specify a name. Example: greet Abdullah")
                continue
            greeting = greet(name)
            print("Agent:", greeting)
            memory.save_context({"input": user_input}, {"output": greeting})
            continue
        except Exception as e:
            print("Agent: Could not greet properly:", e)
            continue

    # Handle name introduction
    if "my name is" in user_input.lower():
        name = user_input.split("is")[-1].strip()
        memory.save_context({"input": user_input}, {"output": name})
        print("Agent:", greet(name))
        continue

    # Handle asking for name
    if "what" in user_input.lower() and "my name" in user_input.lower():
        messages = memory.load_memory_variables({}).get("chat_history", [])
        if messages:
            last_output = messages[-1].content
            print("Agent: You said your name is", last_output)
        else:
            print("Agent: I don't know your name yet.")
        continue

    # Default: use LLM
    try:
        response = llm.invoke(user_input)
        print("Agent:", response.content)
        memory.save_context({"input": user_input}, {"output": response.content})
    except Exception as e:
        print("Error:", e)


C:\Users\user5\PycharmProjects\PythonProject1\.venv\Scripts\python.exe C:\Users\user5\PycharmProjects\PythonProject1\memory_ai.py 
Traceback (most recent call last):
  File "C:\Users\user5\PycharmProjects\PythonProject1\memory_ai.py", line 7, in <module>
    from langchain_openai import ChatOpenAI
  File "C:\Users\user5\PycharmProjects\PythonProject1\.venv\Lib\site-packages\langchain_openai\__init__.py", line 3, in <module>
    from langchain_openai.chat_models import AzureChatOpenAI, ChatOpenAI
  File "C:\Users\user5\PycharmProjects\PythonProject1\.venv\Lib\site-packages\langchain_openai\chat_models\__init__.py", line 3, in <module>
    from langchain_openai.chat_models.azure import AzureChatOpenAI
  File "C:\Users\user5\PycharmProjects\PythonProject1\.venv\Lib\site-packages\langchain_openai\chat_models\azure.py", line 11, in <module>
    from langchain_core.language_models import LanguageModelInput
  File "<frozen importlib._bootstrap>", line 1412, in _handle_fromlist
  File "C:\Users\user5\PycharmProjects\PythonProject1\.venv\Lib\site-packages\langchain_core\language_models\__init__.py", line 99, in __getattr__
    result = import_attr(attr_name, module_name, __spec__.parent)
  File "C:\Users\user5\PycharmProjects\PythonProject1\.venv\Lib\site-packages\langchain_core\_import_utils.py", line 35, in import_attr
    module = import_module(f".{module_name}", package=package)
  File "C:\Users\user5\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user5\PycharmProjects\PythonProject1\.venv\Lib\site-packages\langchain_core\language_models\base.py", line 41, in <module>
    from transformers import GPT2TokenizerFast  # type: ignore[import-not-found]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\user5\PycharmProjects\PythonProject1\.venv\Lib\site-packages\transformers\__init__.py", line 27, in <module>
    from . import dependency_versions_check
  File "C:\Users\user5\PycharmProjects\PythonProject1\.venv\Lib\site-packages\transformers\dependency_versions_check.py", line 16, in <module>
    from .utils.versions import require_version, require_version_core
  File "C:\Users\user5\PycharmProjects\PythonProject1\.venv\Lib\site-packages\transformers\utils\__init__.py", line 24, in <module>
    from .auto_docstring import (
    ...<10 lines>...
    )
  File "C:\Users\user5\PycharmProjects\PythonProject1\.venv\Lib\site-packages\transformers\utils\auto_docstring.py", line 30, in <module>
    from .generic import ModelOutput
  File "C:\Users\user5\PycharmProjects\PythonProject1\.venv\Lib\site-packages\transformers\utils\generic.py", line 51, in <module>
    import torch
  File "C:\Users\user5\PycharmProjects\PythonProject1\.venv\Lib\site-packages\torch\__init__.py", line 281, in <module>
    _load_dll_libraries()
    ~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\user5\PycharmProjects\PythonProject1\.venv\Lib\site-packages\torch\__init__.py", line 264, in _load_dll_libraries
    raise err
OSError: [WinError 1114] A dynamic link library (DLL) initialization routine failed. Error loading "C:\Users\user5\PycharmProjects\PythonProject1\.venv\Lib\site-packages\torch\lib\c10.dll" or one of its dependencies.

Process finished with exit code 1
