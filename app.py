from chalice import Chalice
from application.task_service import TaskService

app = Chalice(app_name='todo_app')

task_service = TaskService()


@app.route('/task', methods=['GET'])
def list_tasks():
    tasks = task_service.list_tasks()
    return {'tasks': tasks}


@app.route('/task', methods=['POST'])
def create_task():
    task = task_service.create_task(app.current_request.json_body)
    return task


@app.route('/task/{task_id}', methods=['GET'])
def get_task(task_id: str):
    task = task_service.get_task(task_id)
    return task


@app.route('/task/{task_id}', methods=['PUT'])
def update_task(task_id: str):
    task = task_service.update_task(task_id, app.current_request.json_body)
    return task


@app.route('/task/{task_id}', methods=['DELETE'])
def delete_task(task_id: str):
    msg = task_service.update_task(task_id, app.current_request.json_body)
    return msg
