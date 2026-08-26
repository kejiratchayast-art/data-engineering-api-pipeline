# Data Engineering API Pipeline

An end-to-end ETL data pipeline that extracts data from a REST API, transforms and validates the data, loads it into PostgreSQL, and performs automated data quality checks.

## Architecture

REST API
↓
Extract
↓
Transform & Validate
↓
Data Quality Checks
↓
PostgreSQL
↓
Docker

## Tech Stack

- Python
- REST API
- PostgreSQL
- SQL
- Pytest
- Docker
- Docker Compose
- Git & GitHub

## Project Structure

data-engineering-api-pipeline/
│
├── data/
│
├── sql/
│   ├── __init__.py
│   ├── database.py
│   └── data_quality.py
│
├── src/
│   ├── api_client.py
│   ├── config.py
│   ├── extract.py
│   ├── pipeline.py
│   └── transform.py
│
├── tests/
│   ├── test_data_quality.py
│   └── test_transform.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pipeline.log
└── README.md

## ETL Pipeline

### 1. Extract

Fetch data from a REST API.

### 2. Transform

Clean and validate the extracted data.

### 3. Load

Load transformed data into a PostgreSQL database.

### 4. Data Quality

Check record counts, NULL values, and duplicate post IDs.

## Data Quality Results

| Metric | Result |
|---|---:|
| Records Extracted | 100 |
| Records Transformed | 100 |
| Records Validated | 100 |
| Records Loaded | 100 |
| NULL Records | 0 |
| Duplicate Post IDs | 0 |

## Testing

Automated tests are implemented using Pytest.

Result: 4 passed

## Docker

The project is containerized using Docker.

PostgreSQL is managed using Docker Compose.

### Start PostgreSQL

docker compose up -d

### Check Running Containers

docker ps

### Run the ETL Pipeline

docker run --rm data-engineering-api-pipeline

Expected result:

ETL PIPELINE COMPLETED SUCCESSFULLY!

## Run Tests

python -m pytest

Expected result:

4 passed

## Logging

Pipeline execution is recorded in pipeline.log.

The log records successful and failed pipeline steps.

## Key Data Engineering Concepts

- ETL Pipeline Development
- REST API Data Extraction
- Data Transformation
- Data Validation
- Data Quality Checks
- PostgreSQL Database Management
- SQL
- Docker Containerization
- Docker Compose
- Automated Testing
- Error Handling
- Retry Mechanism
- Logging
- Idempotent Data Loading

## Future Improvements

- Apache Airflow orchestration
- GitHub Actions CI/CD
- API monitoring
- Data quality monitoring
- Data warehouse integration