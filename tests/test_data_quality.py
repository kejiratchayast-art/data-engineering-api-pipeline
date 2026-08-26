import sqlite3
from sql.data_quality import check_data_quality


def create_test_database(database_file):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE posts (
            user_id INTEGER,
            post_id INTEGER,
            title TEXT,
            body TEXT
        )
    """)

    connection.commit()
    connection.close()


def test_data_quality_pass(tmp_path, capsys):
    database_file = tmp_path / "test.db"

    create_test_database(database_file)

    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    cursor.executemany("""
        INSERT INTO posts (user_id, post_id, title, body)
        VALUES (?, ?, ?, ?)
    """, [
        (1, 1, "Post 1", "Body 1"),
        (1, 2, "Post 2", "Body 2"),
        (2, 3, "Post 3", "Body 3")
    ])

    connection.commit()
    connection.close()

    check_data_quality(str(database_file))

    output = capsys.readouterr().out

    assert "Total records: 3" in output
    assert "Records with NULL values: 0" in output
    assert "Duplicate post IDs: 0" in output


def test_data_quality_detects_null(tmp_path, capsys):
    database_file = tmp_path / "test.db"

    create_test_database(database_file)

    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    cursor.executemany("""
        INSERT INTO posts (user_id, post_id, title, body)
        VALUES (?, ?, ?, ?)
    """, [
        (1, 1, "Post 1", "Body 1"),
        (2, 2, None, "Body 2")
    ])

    connection.commit()
    connection.close()

    check_data_quality(str(database_file))

    output = capsys.readouterr().out

    assert "Total records: 2" in output
    assert "Records with NULL values: 1" in output
    assert "Duplicate post IDs: 0" in output