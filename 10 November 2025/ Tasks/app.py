import streamlit as st
import requests

st.title("🔢🪞 FastAPI + Streamlit Demo")
st.write("Perform maths, reverse words, or get today’s date")

backend_url = "http://127.0.0.1:8000/process"

# Choose action
action = st.selectbox("Choose an action", ["math", "reverse", "date"])

if action == "math":
    st.subheader("🧮 Math Operation")

    # Choose operation
    operation = st.selectbox("Choose operation", ["add", "subtract", "multiply", "divide"])

    # Number of input fields (stored in session)
    if "num_inputs" not in st.session_state:
        st.session_state.num_inputs = 2

    cols = st.columns(2)
    with cols[0]:
        if st.button("➕ Add another number"):
            st.session_state.num_inputs += 1

    with cols[1]:
        if st.button("♻️ Reset numbers"):
            st.session_state.num_inputs = 2

    numbers = []
    for i in range(st.session_state.num_inputs):
        num = st.number_input(f"Enter number {i+1}", value=0.0, key=f"num_{i}")
        numbers.append(num)

    if st.button("Calculate"):
        # Create expression to send to backend
        payload = {"action": "math", "data": f"{operation}:{','.join(map(str, numbers))}"}
        response = requests.post(backend_url, json=payload)
        result = response.json()

        if "result" in result:
            st.success(f"✅ Result: {result['result']}")
        else:
            st.error(result.get("error", "Unknown error"))

elif action == "reverse":
    st.subheader("🔄 Reverse a Word")
    word = st.text_input("Enter a word to reverse:")
    if st.button("Reverse"):
        payload = {"action": "reverse", "data": word}
        response = requests.post(backend_url, json=payload)
        result = response.json()
        st.success(f"🔁 Result: {result['result']}")

elif action == "date":
    st.subheader("📅 Get Today's Date")
    if st.button("Get Date"):
        payload = {"action": "date", "data": ""}
        response = requests.post(backend_url, json=payload)
        result = response.json()
        st.success(f"📆 Today’s Date: {result['result']}")