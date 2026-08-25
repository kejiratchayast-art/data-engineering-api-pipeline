# Data Engineering API Pipeline

A simple ETL data pipeline built with Python.

This project demonstrates how to extract data from an API, transform and validate the data, load it into a SQLite database, and perform data quality checks.

## ETL Pipeline

```text
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
```

## Project Structure

```text
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
```

## Technologies

- Python
- REST API
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

```text
Total records: 100
Records with NULL values: 0
Duplicate post IDs: 0
```

## How to Run

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

Run the complete ETL pipeline:

```bash
python src/pipeline.py
```

Expected output:

```text
ETL PIPELINE COMPLETED SUCCESSFULLY!
```

## Key Data Engineering Concepts

This project demonstrates:

- ETL Pipeline
- API Data Extraction
- Data Transformation
- Data Validation
- Data Quality
- Idempotent Data Loading
- SQLite Database
- Pipeline Automation
- Configuration Management