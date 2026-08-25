import requests
from config import RAW_FILE


def extract_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    for attempt in range(1, 4):
        try:
            print(f"API request attempt {attempt}/3")

            response = requests.get(
                url,
                timeout=10
            )

            response.raise_for_status()

            print("API request successful")

            return response.json()

        except requests.RequestException as error:
            print(f"API request failed: {error}")

            if attempt == 3:
                raise

    return []


def save_raw_data(data, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        import json
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    posts = extract_posts()

    save_raw_data(posts, RAW_FILE)

    print(f"Extracted {len(posts)} posts")
    print(f"Saved raw data to {RAW_FILE}")