import { useState } from "react";
import { addTask } from "../api.js";
export default function AddTaskForm({ onTaskAdded }) {
  const [description, setDescription] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    await addTask({ description, completed: false });
    setDescription("");
    onTaskAdded();
  };

  return (
    <form onSubmit={handleSubmit} className="flex gap-2 mb-4">
      <input
        type="text"
        className="flex-1 border rounded px-2 py-1"
        placeholder="Enter task"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <button className="bg-blue-600 text-white px-4 py-1 rounded">Add</button>
    </form>
  );
}
