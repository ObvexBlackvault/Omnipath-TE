import React, { useEffect, useState } from 'react';
import axios from 'axios';

const AgentPanel = () => {
  const [status, setStatus] = useState({ ForkAlpha: 'unknown', ForkBeta: 'unknown' });

  const fetchStatus = async () => {
    try {
      const response = await axios.get('/api/status');
      setStatus(response.data);
    } catch (error) {
      console.error('Failed to fetch agent status:', error);
    }
  };

  useEffect(() => {
    fetchStatus();
    const interval = setInterval(fetchStatus, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="agent-panel">
      <h2>Agent Status</h2>
      <ul>
        <li><strong>ForkAlpha:</strong> {status.ForkAlpha}</li>
        <li><strong>ForkBeta:</strong> {status.ForkBeta}</li>
      </ul>
    </div>
  );
};

export default AgentPanel;
