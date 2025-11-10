import streamlit as st
import requests

st.title("🔢🪞 FastAPI + Streamlit Demo")
st.write("Perform maths, reverse words, or get today’s date")

backend_url = "http://127.0.0.1:8000/process"

# Choose action
action = st.selectbox("Choose an action", ["math", "reverse", "date"])

if action in ["math", "reverse"]:
    data = st.text_input("Enter your input:")
else:
    data = "none"

if st.button("Submit"):
    payload = {"action": action, "data": data}
    response = requests.post(backend_url, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        if "result" in result:
            st.success(f"✅ Result: {result['result']}")
        else:
            st.error(result.get("error", "Unknown error"))
    else:
        st.error("❌ Failed to reach backend server.")