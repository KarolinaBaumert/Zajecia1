import time
import sqlite3

DB_FILE = "tutorial.db"


def read_tasks():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE status = 'pending'")
        tasks = cursor.fetchall()
    return tasks


def update_task(task_id, new_status):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id))
        conn.commit()


def consume_tasks():
    try:
        while True:
            tasks = read_tasks()

            if tasks:
                task_to_consume = tasks[0]
                task_id = task_to_consume[0]

                print(f"Praca {task_id} jest przetwarzana...")
                update_task(task_id, "in_progress")

                time.sleep(30)

                update_task(task_id, "done")
                print(f"Praca {task_id} została wykonana.")
            else:
                print("Brak prac do wykonania. Konsument czeka...")

            time.sleep(5)
    except KeyboardInterrupt:
        print("\nKonsument zatrzymany przez użytkownika.")


if __name__ == "__main__":
    consume_tasks()
