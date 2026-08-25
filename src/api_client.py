import json
import os
import requests

from config import API_URL, RAW_FILE


def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()

    return response.json()


def save_raw_data(data, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":

    data = fetch_data(API_URL)

    save_raw_data(data, RAW_FILE)

    print(f"Fetched {len(data)} records")
    print(f"Saved raw data to {RAW_FILE}")
    print(data[0])
    