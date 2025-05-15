import axios from "axios";

const BASE_URL = "http://localhost:5000";

export const getTasks = () => axios.get(`${BASE_URL}/tasks`);
export const addTask = (task) => axios.post(`${BASE_URL}/add-task`, task);
export const updateTask = (id, task) =>
  axios.put(`${BASE_URL}/update-task/${id}`, task);
export const deleteTask = (id) => axios.delete(`${BASE_URL}/delete-task/${id}`);
