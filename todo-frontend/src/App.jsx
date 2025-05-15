import TaskList from "./components/TaskList";

function App() {
  return (
    <div className="max-w-xl mx-auto mt-10 px-4">
      <h1 className="text-3xl font-bold text-center mb-6">📝 My To-Do List</h1>
      <TaskList />
    </div>
  );
}

export default App;
