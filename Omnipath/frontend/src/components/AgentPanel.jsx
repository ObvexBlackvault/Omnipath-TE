import React, { useEffect, useState } from 'react';

export default function AgentPanel() {
  const [agents, setAgents] = useState([]);
  const [name, setName] = useState('');

  const fetchAgents = async () => {
    const res = await fetch("http://localhost:5000/api/agents");
    const data = await res.json();
    setAgents(data);
  };

  const registerAgent = async () => {
    const body = {
      agent_id: crypto.randomUUID(),
      name: name || 'Unnamed Agent'
    };

    await fetch("http://localhost:5000/api/agents", {
      method: 'POST',
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });

    setName('');
    fetchAgents();
  };

  useEffect(() => {
    fetchAgents();
  }, []);

  return (
    <div style={{ marginTop: "30px", color: "#0f0" }}>
      <h2>Agent Registry</h2>
      <input
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="New Agent Name"
        style={{ marginRight: "10px" }}
      />
      <button onClick={registerAgent}>Register</button>
      <ul>
        {agents.map(agent => (
          <li key={agent.agent_id}>
            <strong>{agent.name}</strong>  Status: {agent.status}, Priority: {agent.priority_level}
          </li>
        ))}
      </ul>
    </div>
  );
}
