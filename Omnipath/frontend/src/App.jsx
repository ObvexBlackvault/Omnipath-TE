import InputCommand from './components/InputCommand';
import AgentPanel from './components/AgentPanel';

function App() {
  return (
    <div className="max-w-2xl mx-auto mt-10">
      <h1 className="text-3xl font-bold mb-6">Omnipath Control Console</h1>
      <InputCommand />
      <AgentPanel />
    </div>
  );
}

export default App;
