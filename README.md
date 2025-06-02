# Fraud Detection Analysis with Transactional Data

## Overview

This project involves analyzing transactional data collected from Kaggle to detect fraudulent activities across multiple accounts. The goal is to process and transform the data using database normalization and ETL best practices, then visualize insights using Power BI.

## Data Collection & Cleaning

- **Source**: Kaggle transactional dataset.
- **Cleaning Steps**:
    - Converted string timestamps to proper `datetime` formats.
    - Converted numerical fields to appropriate data types.
    - Removed duplicates and handled null values.

## Database Design & ETL

- Applied **Boyce-Codd Normal Form (BCNF)** principles to normalize the data into smaller, well-structured tables.
- Used **Python** to automate:
    - Reading and transforming the CSV data.
    - Loading normalized tables into **MS SQL Server** using insert queries.
- Planned for future scalability by adhering to **ETL architecture** patterns.

## Data Visualization with Power BI

Data from SQL Server was imported into **Power BI** to create an interactive dashboard for insights and fraud detection.

### Power BI Visualizations

- **Bar Chart**: Count of `CustomerOccupation` by occupation.
- **Line Chart**: Average `AccountBalance` by `CustomerAge`.
- **Stacked Column + Line Chart**:
    - Sum of `TransactionAmount` by `CustomerOccupation`.
    - Sum of `AccountBalance` by `CustomerOccupation`.
- **Gauge Chart**: Average `LoginAttempts`.
- **Column Chart**: Count of `TransactionID` by `TransactionDate`.
- **Pie Charts**:
    - Count of `Channel` by channel type.
    - Count of `TransactionType` by type.
- **Column Chart**: Sum of `LoginAttempts` by `TransactionType`.
- **Column Chart**: Count of `TransactionID` by `CustomerAge` and `TransactionType`.

## Future Plans

- Load and scale data processing in **Snowflake**.
- Deploy complete pipeline and dashboards using **Azure Cloud Services**.
- Expand ETL capabilities with orchestration tools and automation.

## Tools & Technologies

- Python (ETL scripting)
- MS SQL Server (Database storage)
- Power BI (Visualization)
- Pandas, NumPy (Data cleaning)
- Snowflake (Future)
- Azure (Future)
