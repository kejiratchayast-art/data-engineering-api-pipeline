import subprocess
import sys
import logging


logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def run_step(description, command):
    print("\n" + "=" * 50)
    print(description)
    print("=" * 50)

    logger.info(description)

    try:
        subprocess.run(
            [sys.executable] + command,
            check=True
        )

        logger.info(f"{description} - SUCCESS")

    except subprocess.CalledProcessError:
        logger.error(f"{description} - FAILED")
        raise


if __name__ == "__main__":

    run_step(
        "STEP 1: Extract data from API",
        ["src/extract.py"]
    )

    run_step(
        "STEP 2: Transform and validate data",
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

    logger.info("ETL PIPELINE COMPLETED SUCCESSFULLY!")
