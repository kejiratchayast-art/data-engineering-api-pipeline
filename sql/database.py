import json
import psycopg2

from src.config import PROCESSED_FILE


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
    cursor.close()


def insert_data(connection, data):
    cursor = connection.cursor()

    for record in data:
        cursor.execute("""
            INSERT INTO posts
            (user_id, post_id, title, body)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (post_id)
            DO UPDATE SET
                user_id = EXCLUDED.user_id,
                title = EXCLUDED.title,
                body = EXCLUDED.body
        """, (
            record["user_id"],
            record["post_id"],
            record["title"],
            record["body"]
        ))

    connection.commit()
    cursor.close()


def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="etl_database",
        user="etl_user",
        password="etl_password"
    )


if __name__ == "__main__":
    data = load_processed_data(PROCESSED_FILE)

    connection = get_connection()

    create_database(connection)
    insert_data(connection, data)

    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM posts")

    count = cursor.fetchone()[0]

    print(f"Loaded {count} records into PostgreSQL")

    cursor.close()
    connection.close()