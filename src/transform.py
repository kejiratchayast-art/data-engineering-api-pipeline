import json
import os

from config import RAW_FILE, PROCESSED_FILE


def load_raw_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def transform_data(data):
    transformed_data = []

    for record in data:
        transformed_record = {
            "user_id": record["userId"],
            "post_id": record["id"],
            "title": record["title"],
            "body": record["body"]
        }

        transformed_data.append(transformed_record)

    return transformed_data


def validate_data(data):
    required_fields = ["user_id", "post_id", "title", "body"]

    for i, record in enumerate(data):

        for field in required_fields:
            if field not in record:
                raise ValueError(
                    f"Record {i} is missing required field: {field}"
                )

        if not isinstance(record["user_id"], int):
            raise ValueError(
                f"Record {i}: user_id must be an integer"
            )

        if not isinstance(record["post_id"], int):
            raise ValueError(
                f"Record {i}: post_id must be an integer"
            )

        if not record["title"]:
            raise ValueError(
                f"Record {i}: title is empty"
            )

        if not record["body"]:
            raise ValueError(
                f"Record {i}: body is empty"
            )

    print(f"Validation passed: {len(data)} records")


def save_processed_data(data, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":

    data = load_raw_data(RAW_FILE)

    transformed_data = transform_data(data)

    validate_data(transformed_data)

    save_processed_data(transformed_data, PROCESSED_FILE)

    print(f"Transformed {len(transformed_data)} records")
    print(f"Saved processed data to {PROCESSED_FILE}")
    print(transformed_data[0])