from bson import ObjectId
from config.connection import db
from models.task_model import TaskModel

all_tasks = db["tasks"]

# ADD
def add_task(task_data: dict):
    task = TaskModel(**task_data)
    result = all_tasks.insert_one(task.dict())
    return str(result.inserted_id)

# GET ALL
def get_all_tasks():
    tasks = []
    for task in all_tasks.find():
        tasks.append({
            "id": str(task["_id"]),
            "description": task["description"],
            "status": task["status"]
        })
    return tasks

# UPDATE
def update_task(task_id: str, updated_data: dict):
    task = TaskModel(**updated_data)
    result = all_tasks.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": task.dict()}
    )
    return result.modified_count > 0

# DELETE
def del_task(task_id: str):
    result = all_tasks.delete_one({"_id": ObjectId(task_id)})
    return result.deleted_count > 0
