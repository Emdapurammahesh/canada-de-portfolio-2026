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

## 📂 Project 2: E-Commerce Sales Processor (File Ingestion) - [IN PROGRESS]
**Goal:** Automateing the cleaning and loading of "dirty" CSV sales drops.
- **Techniques:** Pandas for Data Profiling, Duplicate Removal, and NULL handling.
- **Status:** Currently building the transformation logic.
