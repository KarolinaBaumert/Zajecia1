import csv
import uuid
from datetime import datetime

TASKS_FILE = "tasks.csv"


def create_task():
    task_id = str(uuid.uuid4())
    task = {
        "id": task_id,
        "description": "Wykonaj rozmowę telefoniczną",
        "status": "pending",
        "created_at": datetime.now().isoformat()
    }


    with open(TASKS_FILE, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=task.keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(task)

    print(f"Praca {task_id} została dodana z opisem: {task['description']}")


if __name__ == "__main__":
    create_task()
