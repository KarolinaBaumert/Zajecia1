import uuid
from datetime import datetime
import sqlite3

DB_FILE = "tutorial.db"


def initialize_db():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id TEXT PRIMARY KEY,
                description TEXT,
                status TEXT,
                created_at TEXT
            )
        """)
        conn.commit()


def create_task():
    task_id = str(uuid.uuid4())
    task = {
        "id": task_id,
        "description": "Wykonaj rozmowę telefoniczną",
        "status": "pending",
        "created_at": datetime.now().isoformat()
    }

    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tasks (id, description, status, created_at)
            VALUES (:id, :description, :status, :created_at)
        """, task)
        conn.commit()

    print(f"Praca {task_id} została dodana z opisem: {task['description']}")


if __name__ == "__main__":
    initialize_db()
    create_task()
