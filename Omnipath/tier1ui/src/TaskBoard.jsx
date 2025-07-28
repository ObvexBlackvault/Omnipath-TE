import React, { useEffect, useState } from 'react';

const TaskBoard = () => {
  const [tasks, setTasks] = useState([]);
  const [error, setError] = useState(null);

  // Fetch tasks from backend on component load
  useEffect(() => {
    fetch('http://localhost:5000/api/tasks')  // Adjust port if your Flask backend runs on another port
      .then(res => {
        if (!res.ok) throw new Error('Network response was not ok');
        return res.json();
      })
      .then(data => setTasks(data))
      .catch(err => {
        console.error('Fetch error:', err);
        setError('Could not load tasks');
      });
  }, []);

  return (
    <div>
      <h1>TaskBoard</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <ul>
        {tasks.map((task, idx) => (
          <li key={idx}>{task.title || 'Untitled Task'}</li>
        ))}
      </ul>
    </div>
  );
};

export default TaskBoard;
