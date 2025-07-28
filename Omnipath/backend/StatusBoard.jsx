
import React, { useEffect, useState } from 'react';

export default function StatusBoard() {
  const [log, setLog] = useState([]);

  useEffect(() => {
    const fetchStatus = () => {
      fetch('http://localhost:5000/api/status')
        .then(res => res.json())
        .then(data => setLog(data.log || []));
    };
    fetchStatus();
    const interval = setInterval(fetchStatus, 3000); // Poll every 3s
    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h2>System Status</h2>
      <ul>
        {log.map((entry, idx) => (
          <li key={idx}>{entry}</li>
        ))}
      </ul>
    </div>
  );
}
