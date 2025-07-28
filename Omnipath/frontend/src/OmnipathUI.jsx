import React, { useEffect, useState, useRef } from 'react';

export default function OmnipathUI() { const [logs, setLogs] = useState([]); const [command, setCommand] = useState(''); const [history, setHistory] = useState([]); const [historyIndex, setHistoryIndex] = useState(-1); const terminalRef = useRef(null);

useEffect(() => { const fetchLogs = async () => { try { const res = await fetch("http://localhost:5000/api/status"); const data = await res.json(); setLogs((prevLogs) => [...prevLogs.slice(-99), ...data.logs]); } catch (err) { setLogs((prevLogs) => [...prevLogs.slice(-99), ERROR: ${err.message}]); } }; const interval = setInterval(fetchLogs, 2000); return () => clearInterval(interval); }, []);

useEffect(() => { if (terminalRef.current) { terminalRef.current.scrollTop = terminalRef.current.scrollHeight; } }, [logs]);

const sendCommand = async (e) => { e.preventDefault(); try { await fetch("http://localhost:5000/api/command", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ command, args: [] }) }); setLogs(prev => [...prev, > ${command}]); setHistory(prev => [...prev, command]); setCommand(''); setHistoryIndex(-1); } catch (err) { setLogs(prev => [...prev, COMMAND ERROR: ${err.message}]); } };

return ( <div className="bg-black text-green-400 font-mono p-4 rounded-lg h-screen overflow-hidden flex flex-col"> <div className="flex-1 overflow-y-scroll border border-green-600 rounded-md p-2" ref={terminalRef}> {logs.map((line, index) => ( <div key={index} className="whitespace-pre-wrap animate-pulse-flicker">{line}</div> ))} </div> <form onSubmit={sendCommand} className="mt-4"> <input value={command} onChange={(e) => setCommand(e.target.value)} onKeyDown={(e) => { if (e.key === 'ArrowUp') { if (historyIndex < history.length - 1) { const newIndex = historyIndex + 1; setCommand(history[history.length - 1 - newIndex]); setHistoryIndex(newIndex); } } else if (e.key === 'ArrowDown') { if (historyIndex > 0) { const newIndex = historyIndex - 1; setCommand(history[history.length - 1 - newIndex]); setHistoryIndex(newIndex); } else { setCommand(''); setHistoryIndex(-1); } } }} placeholder="> enter directive..." className="w-full bg-black border border-green-400 text-lime-300 px-4 py-2 rounded-md outline-none font-mono focus:ring-2 focus:ring-cyan-500 animate-glyph" /> </form> </div> ); }


