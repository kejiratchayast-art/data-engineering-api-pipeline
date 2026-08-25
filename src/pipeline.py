import subprocess
import sys

def run_step(description, command):
    print("\n" + "=" * 50)
    print(description)
    print("=" * 50)

    subprocess.run(
        [sys.executable] + command,
        check=True
    )

if __name__ == "__main__":

    run_step(
        "STEP 1: Extract data from API",
        ["src/api_client.py"]
    )

    run_step(
        "STEP 2: Transform data",
        ["src/transform.py"]
    )

    run_step(
    "STEP 3: Load data into database",
    ["-m", "sql.database"]
    )

    run_step(
    "STEP 4: Check data quality",
    ["-m", "sql.data_quality"]
    )

    print("\n" + "=" * 50)
    print("ETL PIPELINE COMPLETED SUCCESSFULLY!")
    print("=" * 50)