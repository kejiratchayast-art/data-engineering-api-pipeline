# Data Engineering API Pipeline

A simple ETL data pipeline built with Python.

This project demonstrates how to extract data from an API, transform and validate the data, load it into a SQLite database, and perform data quality checks.

## ETL Pipeline

API
↓
Extract
↓
Raw JSON
↓
Transform
↓
Validation
↓
Processed JSON
↓
SQLite Database
↓
Data Quality Check

## Project Structure

data-engineering-api-pipeline/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── posts.db
│
├── src/
│   ├── api_client.py
│   ├── config.py
│   ├── extract.py
│   ├── pipeline.py
│   └── transform.py
│
├── sql/
│   ├── database.py
│   └── data_quality.py
│
├── .gitignore
├── README.md
└── requirements.txt

## Technologies

- Python
- REST API
- Requests
- JSON
- SQLite
- SQL
- Git / GitHub

## Pipeline Steps

### 1. Extract

Fetch data from the JSONPlaceholder API and save the raw data as JSON.

### 2. Transform

Transform the API response into a clean and consistent structure.

### 3. Validation

Validate the transformed data before loading it into the database.

### 4. Load

Load the processed data into a SQLite database.

### 5. Data Quality

Check the database for:

- Total records
- NULL values
- Duplicate post IDs

## Data Quality Result

The pipeline successfully processed 100 records.

Total records: 100
Records with NULL values: 0
Duplicate post IDs: 0

## Error Handling

The API extraction process includes a retry mechanism.

If an API request fails, the pipeline will retry the request up to 3 times before returning an error.

API request attempt 1/3
API request attempt 2/3
API request attempt 3/3

## Logging

Pipeline execution is recorded in:

pipeline.log

The log records successful and failed pipeline steps.

## How to Run

### 1. Activate the virtual environment

Windows PowerShell:

.venv\Scripts\Activate.ps1

### 2. Install dependencies

pip install -r requirements.txt

### 3. Run the complete ETL pipeline

python src/pipeline.py

## Expected Output

STEP 1: Extract data from API
API request successful
Extracted 100 posts

STEP 2: Transform data
Validation passed: 100 records
Transformed 100 records

STEP 3: Load data into database
Loaded 100 records into database

STEP 4: Check data quality
Total records: 100
Records with NULL values: 0
Duplicate post IDs: 0

==================================================
ETL PIPELINE COMPLETED SUCCESSFULLY!
==================================================

## Key Data Engineering Concepts

This project demonstrates:

- ETL Pipeline
- API Data Extraction
- Data Transformation
- Data Validation
- Data Quality Checks
- Idempotent Data Loading
- SQLite Database
- Pipeline Automation
- Configuration Management
- Error Handling
- Retry Mechanism
- Logging

## Project Result

100 records extracted
        ↓
100 records transformed
        ↓
100 records validated
        ↓
100 records loaded
        ↓
0 NULL records
0 duplicate IDs