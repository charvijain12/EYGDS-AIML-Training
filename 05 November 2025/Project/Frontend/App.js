import React, { useState } from "react";

function App() {
  const [employee, setEmployee] = useState("charvi");
  const [recommendations, setRecommendations] = useState([]);
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);

  const getRecommendations = async () => {
    const res = await fetch(`http://127.0.0.1:8000/recommend/${employee}`);
    const data = await res.json();
    setRecommendations(data.recommendations);
  };

  const sendMessage = async () => {
    const res = await fetch(`http://127.0.0.1:8000/chat?message=${message}`, { method: "POST" });
    const data = await res.json();
    setChat([...chat, { user: "You", text: message }, { user: "Bot", text: data.reply }]);
    setMessage("");
  };

  return (
    <div style={{ margin: "2rem" }}>
      <h2>Internal Project Matching Chatbot</h2>
      <button onClick={getRecommendations}>Get Recommendations</button>
      <ul>
        {recommendations.map((r, i) => (
          <li key={i}>{r.project} - Match: {r.match_score}%</li>
        ))}
      </ul>

      <div style={{ marginTop: "2rem" }}>
        <h3>Chatbot</h3>
        <div style={{ border: "1px solid #aaa", padding: "10px", width: "300px", height: "200px", overflowY: "scroll" }}>
          {chat.map((c, i) => (
            <p key={i}><b>{c.user}:</b> {c.text}</p>
          ))}
        </div>
        <input value={message} onChange={e => setMessage(e.target.value)} placeholder="Type here..." />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default App;