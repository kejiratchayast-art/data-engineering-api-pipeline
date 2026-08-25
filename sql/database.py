import json
import sqlite3

from src.config import PROCESSED_FILE, DATABASE_FILE


def load_processed_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def create_database(connection):
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            user_id INTEGER,
            post_id INTEGER PRIMARY KEY,
            title TEXT,
            body TEXT
        )
    """)

    connection.commit()


def insert_data(connection, data):
    cursor = connection.cursor()

    for record in data:
        cursor.execute("""
            INSERT OR REPLACE INTO posts
            (user_id, post_id, title, body)
            VALUES (?, ?, ?, ?)
        """, (
            record["user_id"],
            record["post_id"],
            record["title"],
            record["body"]
        ))

    connection.commit()


if __name__ == "__main__":

    data = load_processed_data(PROCESSED_FILE)

    connection = sqlite3.connect(DATABASE_FILE)

    create_database(connection)

    insert_data(connection, data)

    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM posts")

    count = cursor.fetchone()[0]

    print(f"Loaded {count} records into database")

    connection.close()