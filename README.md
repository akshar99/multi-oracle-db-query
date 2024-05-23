# Multi DB Query Runner

## Description
This repository contains a Python script to run health check queries on multiple Oracle databases and generate reports. 
This script can also be used to run DDL,DML,DCL queries as well. One needs to be cautious while using on these. 
The script connects to specified databases, executes a query, and saves the results in a CSV file.

## Features
- Connects to multiple Oracle databases.
- Executes a generic health check query.
- Handles various connection and query execution errors.
- Stores results in a pandas DataFrame.
- Saves the results as a CSV report.

## Requirements
- Python 3.11 and above 
- `oracledb` library
- `pandas` library

## Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/akshar99/multi-oracle-db-query/
    cd multi-oracle-db-query
    ```
2. Install required libraries:
    ```bash
    pip install oracledb pandas
    ```
3. Update the script with your database credentials and server details.
4. Run the script:
    ```bash
    python db_health_check.py
    ```

