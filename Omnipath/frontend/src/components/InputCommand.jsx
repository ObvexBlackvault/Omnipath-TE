import React, { useState } from "react";
import axios from "axios";

const InputCommand = () => {
  const [input, setInput] = useState("");
  const [status, setStatus] = useState("");

  const sendCommand = async () => {
    try {
      const response = await axios.post("/api/command", { command: input });
      setStatus(response.data.message || "Command executed.");
    } catch (error) {
      console.error(error);
      setStatus("Failed to send command.");
    }
  };

  return (
    <div className="input-container">
      <input
        type="text"
        placeholder="Enter command..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <button onClick={sendCommand}>Send</button>
      {status && <p>{status}</p>}
    </div>
  );
};

export default InputCommand;
