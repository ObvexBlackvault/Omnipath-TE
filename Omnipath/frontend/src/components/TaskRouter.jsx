import React from 'react';

const TaskRouter = ({ task }) => {
  const handleTask = () => {
    switch (task.title) {
      case 'Boot OmniAgent':
        console.log('Initializing OmniAgent...');
        break;
      case 'Link memory sync':
        console.log('Syncing memory modules...');
        break;
      case 'Deploy tracking node':
        console.log('Deploying node to active grid...');
        break;
      default:
        console.log('Unknown task:', task.title);
    }
  };

  return (
    <div
      onClick={handleTask}
      style={{
        background: '#111',
        color: '#0f0',
        padding: '10px',
        margin: '10px 0',
        border: '1px solid #0f0',
        fontFamily: 'monospace',
        cursor: 'pointer',
      }}
    >
      {task.title}
    </div>
  );
};

export default TaskRouter;
