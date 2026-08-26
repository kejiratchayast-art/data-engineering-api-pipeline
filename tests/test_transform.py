import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from transform import transform_data, validate_data


def test_transform_data():
    raw_data = [
        {
            "userId": 1,
            "id": 101,
            "title": "Test Post",
            "body": "Test body"
        }
    ]

    result = transform_data(raw_data)

    assert result[0]["user_id"] == 1
    assert result[0]["post_id"] == 101
    assert result[0]["title"] == "Test Post"
    assert result[0]["body"] == "Test body"


def test_validate_data():
    data = [
        {
            "user_id": 1,
            "post_id": 101,
            "title": "Test Post",
            "body": "Test body"
        }
    ]

    validate_data(data)