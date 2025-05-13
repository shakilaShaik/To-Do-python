from config.connection.db import db
from models.task_model import TaskModel
all_tasks=db["tasks"]
def add_task(task_data: dict):
    task= TaskModel(task_data)
    result= all_tasks.insert_one(task.dict())
    return str(result.inserted_id)