import React, { useState } from 'react'; import TaskRouter from './TaskRouter'; import SVGTerminalOverlay from './SVGTerminalOverlay';

export default function InputCommand() { const [tasks, setTasks] = useState([]); const [input, setInput] = useState('');

const handleSubmit = (e) => { e.preventDefault(); if (input.trim() === '') return;

const newTask = {
  id: Date.now(),
  command: input,
};

setTasks(prev => [...prev, newTask]);
setInput('');

};

return ( <div style={{ position: 'relative', width: '100vw', height: '100vh', background: '#000', overflow: 'hidden' }}> <SVGTerminalOverlay /> <div style={{ position: 'relative', zIndex: 10, padding: '20px', color: '#0f0', fontFamily: 'monospace' }}> <h1>Omnipath Command Terminal</h1> <form onSubmit={handleSubmit}> <input type="text" value={input} onChange={(e) => setInput(e.target.value)} placeholder="Enter command..." style={{ background: 'black', color: '#0f0', border: '1px solid #0f0', padding: '10px', fontFamily: 'monospace', width: '300px' }} /> </form> <div style={{ marginTop: '20px' }}> {tasks.map(task => ( <TaskRouter key={task.id} task={task} /> ))} </div> </div> </div> ); }


