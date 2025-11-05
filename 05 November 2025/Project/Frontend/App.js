import React, { useState } from "react";

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);

  // send message to backend
  const sendMessage = async () => {
    if (!input.trim()) return;

    // show user message immediately
    const newMessages = [...messages, { sender: "You", text: input }];
    setMessages(newMessages);
    setInput("");

    try {
      // backend call
      const response = await fetch(`http://127.0.0.1:8000/chat/${input}`);
      const data = await response.json();

      // add bot reply to chat
      setMessages([...newMessages, { sender: "Bot", text: data.reply }]);
    } catch (error) {
      setMessages([
        ...newMessages,
        { sender: "Bot", text: "Error connecting to server 😕" },
      ]);
    }
  };

  return (
    <div style={{ margin: "40px" }}>
      <h2>Internal Project Matching Chatbot</h2>

      <div
        style={{
          border: "1px solid #ccc",
          padding: "10px",
          width: "400px",
          height: "300px",
          overflowY: "scroll",
          marginBottom: "10px",
        }}
      >
        {messages.map((msg, idx) => (
          <p key={idx}>
            <strong>{msg.sender}: </strong> {msg.text}
          </p>
        ))}
      </div>

      <input
        type="text"
        value={input}
        placeholder="Type here..."
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && sendMessage()}
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}

export default App;