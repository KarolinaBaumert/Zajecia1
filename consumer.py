import csv
import time


TASKS_FILE = "tasks.csv"


def read_tasks():
    tasks = []
    try:
        with open(TASKS_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            tasks = [row for row in reader]
    except FileNotFoundError:
        print("Brak pliku z zadaniami. Consumer czeka na zadania...")
    return tasks


def update_task(task_id, new_status):
    tasks = read_tasks()
    with open(TASKS_FILE, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "description", "status", "created_at"])
        writer.writeheader()
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = new_status
            writer.writerow(task)


def consume_tasks():
    while True:
        tasks = read_tasks()
        pending_tasks = [task for task in tasks if task["status"] == "pending"]

        if pending_tasks:
            task_to_consume = pending_tasks[0]
            task_id = task_to_consume["id"]

            print(f"Praca {task_id} jest przetwarzana...")
            update_task(task_id, "in_progress")

            time.sleep(30)

            update_task(task_id, "done")
            print(f"Praca {task_id} została wykonana.")
        else:
            print("Brak prac do wykonania. Consumer czeka...")

        time.sleep(5)


if __name__ == "__main__":
    consume_tasks()
