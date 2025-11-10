import streamlit as st
import requests

st.title("FastAPI + Streamlit + AI Integration")
st.write("Perform math operations, reverse words, get today's date, or analyze text using an AI model through FastAPI.")

# Update this if backend runs elsewhere
backend_url = "http://127.0.0.1:8000/process"

# Select the feature
action = st.selectbox("Choose an action", ["math", "reverse", "date", "ai"])

# ---------------------------
# Math Operation
# ---------------------------
if action == "math":
    st.subheader("Math Operation")

    operation = st.selectbox("Choose operation", ["add", "subtract", "multiply", "divide"])

    if "num_inputs" not in st.session_state:
        st.session_state.num_inputs = 2

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Add another number"):
            st.session_state.num_inputs += 1
    with col2:
        if st.button("Reset numbers"):
            st.session_state.num_inputs = 2

    numbers = []
    for i in range(st.session_state.num_inputs):
        num = st.number_input(f"Enter number {i + 1}", value=0.0, key=f"num_{i}")
        numbers.append(num)

    if st.button("Calculate"):
        payload = {"action": "math", "data": f"{operation}:{','.join(map(str, numbers))}"}
        try:
            response = requests.post(backend_url, json=payload)
            result = response.json()
            if "result" in result:
                st.success(f"Result: {result['result']}")
            else:
                st.error(result.get("error", "Unknown error"))
        except Exception as e:
            st.error(f"Error connecting to backend: {e}")

# ---------------------------
# Reverse a word
# ---------------------------
elif action == "reverse":
    st.subheader("Reverse a Word")
    word = st.text_input("Enter a word:")
    if st.button("Reverse"):
        payload = {"action": "reverse", "data": word}
        try:
            response = requests.post(backend_url, json=payload)
            result = response.json()
            if "result" in result:
                st.success(f"Reversed: {result['result']}")
            else:
                st.error(result.get("error", "Unknown error"))
        except Exception as e:
            st.error(f"Error connecting to backend: {e}")

# ---------------------------
# Get today's date
# ---------------------------
elif action == "date":
    st.subheader("Today's Date")
    if st.button("Get Date"):
        payload = {"action": "date", "data": ""}
        try:
            response = requests.post(backend_url, json=payload)
            result = response.json()
            if "result" in result:
                st.success(f"Today's Date: {result['result']}")
            else:
                st.error(result.get("error", "Unknown error"))
        except Exception as e:
            st.error(f"Error connecting to backend: {e}")

# ---------------------------
# AI Text Analysis (via OpenAI model in FastAPI)
# ---------------------------
elif action == "ai":
    st.subheader("AI Text Analysis")
    text = st.text_area("Enter your text here:")
    if st.button("Analyze"):
        payload = {"action": "ai", "data": text}
        try:
            response = requests.post(backend_url, json=payload)
            result = response.json()
            if "result" in result:
                st.success(f"AI Response: {result['result']}")
            else:
                st.error(result.get("error", "Unknown error"))
        except Exception as e:
            st.error(f"Error connecting to backend: {e}")