import React, { useState } from 'react';
import TaskRouter from './components/TaskRouter';
import SVGTerminalOverlay from './components/SVGTerminalOverlay';
import InputCommand from './components/InputCommand';
import AgentPanel from './components/AgentPanel';


function App() {
  const [tasks, setTasks] = useState([]);

  const handleCommand = (commandText) => {
    const newTask = {
      id: Date.now(),
      command: commandText,
      args: [],
      status: 'queued',
      logs: [`Command received: "${commandText}"`]
    };
    setTasks((prev) => [...prev, newTask]);
  };

  return (
    <div style={{ position: 'relative', width: '100vw', height: '100vh', background: '#000', overflow: 'hidden' }}>
      <SVGTerminalOverlay />
      <div style={{ position: 'relative', zIndex: 10, padding: '20px', color: '#0f0', fontFamily: 'monospace' }}>
        <h1>Omnipath LIVE FEED</h1>
        {tasks.map(task => (
          <TaskRouter key={task.id} task={task} />
        ))}
        <InputCommand onCommand={handleCommand} />
       <AgentPanel />
      </div>
    </div>
  );
}

export default App;
