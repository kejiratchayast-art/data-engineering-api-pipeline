# Data Engineering API Pipeline

An end-to-end ETL data pipeline that extracts data from an API, transforms and validates the data, loads it into a SQLite database, and performs automated data quality checks.

## Architecture

API ? Extract ? Transform & Validate ? SQLite Database ? Data Quality Checks ? Automated Tests

## Tech Stack

- Python
- REST API
- SQLite
- SQL
- Pytest
- Git & GitHub

## Project Structure

data-engineering-api-pipeline/
+-- data/
+-- sql/
¦   +-- __init__.py
¦   +-- database.py
¦   +-- data_quality.py
+-- src/
¦   +-- api_client.py
¦   +-- config.py
¦   +-- extract.py
¦   +-- pipeline.py
¦   +-- transform.py
+-- tests/
¦   +-- test_data_quality.py
¦   +-- test_transform.py
+-- requirements.txt
+-- pipeline.log
+-- README.md

## ETL Pipeline

### 1. Extract
Fetch data from a REST API.

### 2. Transform
Clean and validate the extracted data.

### 3. Load
Store transformed data in a SQLite database.

### 4. Data Quality
Check total records, NULL values, and duplicate post IDs.

## Data Quality Result

- Total records: 100
- NULL records: 0
- Duplicate post IDs: 0

## Testing

Pytest result: 4 passed.

## Run the Pipeline

    python src/pipeline.py

## Logging

Pipeline execution is recorded in pipeline.log.

## Future Improvements

- PostgreSQL support
- Docker
- Apache Airflow
- GitHub Actions CI/CD
- API monitoring
- Data quality monitoring
