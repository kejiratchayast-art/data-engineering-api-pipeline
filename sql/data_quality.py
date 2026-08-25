import sqlite3


def check_data_quality(database_file):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    # 1. Check total records
    cursor.execute("SELECT COUNT(*) FROM posts")
    total_records = cursor.fetchone()[0]

    print(f"Total records: {total_records}")

    # 2. Check NULL values
    cursor.execute("""
        SELECT COUNT(*)
        FROM posts
        WHERE user_id IS NULL
           OR post_id IS NULL
           OR title IS NULL
           OR body IS NULL
    """)

    null_records = cursor.fetchone()[0]

    print(f"Records with NULL values: {null_records}")

    # 3. Check duplicate post IDs
    cursor.execute("""
        SELECT COUNT(*) - COUNT(DISTINCT post_id)
        FROM posts
    """)

    duplicate_records = cursor.fetchone()[0]

    print(f"Duplicate post IDs: {duplicate_records}")

    connection.close()


if __name__ == "__main__":
    database_file = "data/posts.db"

    check_data_quality(database_file)