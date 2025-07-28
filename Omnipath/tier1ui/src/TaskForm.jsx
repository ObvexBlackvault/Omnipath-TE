import React, { useState } from "react";

export default function TaskForm({ onCreated }) {
  const [name, setName] = useState("");
  const [agent, setAgent] = useState("");

  const submit = e => {
    e.preventDefault();
    fetch("/api/task/create", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, agent })
    })
      .then(res => res.json())
      .then(task => {
        onCreated(task);
        setName("");
        setAgent("");
      });
  };

  return (
    <form onSubmit={submit} style={{ display: "flex", gap: 10 }}>
      <input value={name} onChange={e => setName(e.target.value)} placeholder="Task Name" required />
      <input value={agent} onChange={e => setAgent(e.target.value)} placeholder="Agent" required />
      <button type="submit">Create Task</button>
    </form>
  );
}
