import { useEffect, useState } from "react";
import { getTasks, deleteTask, updateTask } from "../api.js";
import AddTaskForm from "./AddTaskForm";

export default function TaskList() {
  const [tasks, setTasks] = useState([]);

  const fetchTasks = async () => {
    const res = await getTasks();
    setTasks(res.data.tasks);
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  const handleDelete = async (id) => {
    await deleteTask(id);
    fetchTasks();
  };

  const toggleComplete = async (task) => {
    await updateTask(task._id, {
      description: task.description,
      completed: !task.completed,
    });
    fetchTasks();
  };

  return (
    <div>
      <AddTaskForm onTaskAdded={fetchTasks} />
      <ul className="space-y-2">
        {tasks.map((task) => (
          <li
            key={task._id}
            className="flex justify-between items-center border px-3 py-2 rounded">
            <span
              className={`cursor-pointer ${
                task.completed ? "line-through text-gray-500" : ""
              }`}
              onClick={() => toggleComplete(task)}>
              {task.description}
            </span>
            <button
              onClick={() => handleDelete(task._id)}
              className="text-red-500 font-bold">
              X
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
