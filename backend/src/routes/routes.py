from flask import Blueprint, request, jsonify
from tasks.tasks import add_task, update_task, del_task, get_all_tasks

task_bp = Blueprint("task_bp", __name__)

# CREATE
@task_bp.route("/add-task", methods=["POST"])
def create_task_route():
    try:
        task_data = request.get_json()
        inserted_id = add_task(task_data)
        return jsonify({"message": "Task added successfully", "id": inserted_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# READ ALL TASKS
@task_bp.route("/get-tasks", methods=["GET"])
def get_tasks_route():
    try:
        tasks = get_all_tasks()
        return jsonify({"tasks": tasks}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# UPDATE
@task_bp.route("/update-task", methods=["PUT"])
def update_task_route():
    try:
        updated_data = request.get_json()
        if not updated_data or "id" not in updated_data:
            return jsonify({"error": "Missing 'id' in request body"}), 400

        task_id = updated_data.pop("id")
        updated = update_task(task_id, updated_data)
        return jsonify({"message": "Task updated", "updated": updated}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# DELETE
@task_bp.route("/delete-task", methods=["DELETE"])
def delete_task_route():
    try:
        data = request.get_json()
        if not data or "id" not in data:
            return jsonify({"error": "Missing 'id' in request body"}), 400

        task_id = data["id"]
        deleted = del_task(task_id)

        if deleted:
            return jsonify({"message": "Task deleted successfully"}), 200
        else:
            return jsonify({"error": "Task not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400
