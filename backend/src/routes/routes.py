from flask import Blueprint, request, jsonify
from tasks.tasks import add_task
task_bp= Blueprint("task_bp" , __name__)
@task_bp.route("/add-task" , methods=["POST"])
def create_task():
    try:
        task_data = request.get_json()
        inserted_id = add_task(task_data)
        return jsonify({"message":" Added the task", "id": inserted_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400