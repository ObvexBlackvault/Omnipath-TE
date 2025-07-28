import React, { useState } from 'react';

const TaskRouter = ({ onRoute }) => { const [taskName, setTaskName] = useState(''); const [target, setTarget] = useState('');

const handleRoute = (e) => { e.preventDefault(); if (taskName && target) { onRoute({ task: taskName, target }); setTaskName(''); setTarget(''); } };

return ( <div className="bg-gray-900 p-4 border border-indigo-500 rounded-md"> <h2 className="text-indigo-300 text-lg font-bold mb-2">Task Router</h2> <form onSubmit={handleRoute} className="space-y-2"> <input type="text" placeholder="Task name..." value={taskName} onChange={(e) => setTaskName(e.target.value)} className="w-full p-2 bg-black border border-indigo-600 text-white rounded-md" /> <input type="text" placeholder="Target fork..." value={target} onChange={(e) => setTarget(e.target.value)} className="w-full p-2 bg-black border border-indigo-600 text-white rounded-md" /> <button type="submit" className="w-full bg-indigo-600 hover:bg-indigo-700 text-white py-2 px-4 rounded-md"> Route Task </button> </form> </div> ); };

export default TaskRouter;


