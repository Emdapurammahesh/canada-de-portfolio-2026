# Data Engineering Portfolio: 4 End-to-End Pipelines

This repository contains 4 distinct data engineering projects demonstrating different ingestion techniques, data processing styles, and storage solutions.

---

## 📊 Project 1: Real-Time Crypto Market Tracker (API Ingestion)
**Goal:** Build a robust ETL pipeline to track cryptocurrency price fluctuations in real-time.

### 🏗️ Architecture
- **Source:** [CoinGecko REST API](https://www.coingecko.com/en/api)
- **Ingestion:** Python `requests` with error handling and metadata injection.
- **Storage:** Local JSON (Landing Zone) and SQLite (Relational Warehouse).
- **Orchestration:** Custom Python Master Script with a time-loop for live tracking.

### 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** `requests`, `sqlite3`, `json`, `datetime`
- **Database:** SQLite

### 📋 Key Engineering Features
* **Idempotency:** Designed to append data without overwriting history.
* **Data Flattening:** Transformed nested JSON structures into a relational 2D format.
* **Metadata Auditing:** Every row includes an `extracted_at` timestamp for time-series analysis.
* **Fault Tolerance:** Implemented `try-except` blocks to handle API timeouts or network errors.

### 🚀 How to Run
1. Clone the repo.
2. Initialize the virtual environment: `source venv/bin/activate`.
3. Install dependencies: `pip install requests`.
4. Execute the orchestrator: `python run_pipeline.py`.

---

## 📂 Project 2: E-Commerce Sales Processor (File Ingestion) 

# End-to-End Medallion Data Pipeline with PySpark

## 📌 Project Overview
This project implements a professional **Medallion Architecture** data pipeline using **PySpark**. It automates the transition of raw e-commerce sales data into business-ready insights. The system is designed to be **Cloud-Ready**, utilizing environment-agnostic configurations and high-performance storage formats.

## 🏗️ Architecture: The Medallion Layers
1. **Bronze (Raw):** Ingests raw `CSV` data exactly as it arrives from source systems.
2. **Silver (Cleaned):** De-duplicates records, handles missing values (Nulls), and converts data to **Apache Parquet** for optimized storage.
3. **Gold (Analytics):** Aggregates data to calculate key business metrics like Total Revenue and Units Sold per product.

## 🛠️ Tech Stack
* **Language:** Python 3.14
* **Engine:** Apache Spark 4.1.1 (PySpark)
* **Environment:** Java 17 (OpenJDK)
* **Format:** Parquet (Snappy Compressed)
* **Orchestration:** Custom Python Wrapper with Logging

## 🚀 Key Features
* **Custom Orchestration:** A `main_pipeline.py` script that manages job execution, tracks processing time, and handles errors.
* **Environment Decoupling:** All file paths and system metadata are stored in a centralized `config.json`, allowing the pipeline to move between Local, Dev, and Prod environments without code changes.
* **Data Quality Logic:** Automated removal of duplicate transaction IDs and filtering of incomplete financial records.
* **Storage Optimization:** Transitioned from row-based CSV to columnar-based Parquet, reducing storage footprint and increasing query speed.

## 📂 Project Structure
```text
.
├── main_pipeline.py        # Master Orchestrator (Entry Point)
├── config.json             # Environment & Path Configurations
├── data_lake/              # Simulated Data Lake
│   ├── 01_bronze_raw/      # Raw CSV Landings
│   ├── 02_silver_cleaned/  # Cleaned Parquet Files
│   └── 03_gold_analytics/  # Aggregated Business Tables
├── src/pyspark_jobs/       # Modular PySpark Logic
│   ├── ingest_bronze_to_silver.py
│   └── aggregate_silver_to_gold.py
└── venv/                   # Isolated Python Environment
