# API-Based ETL Pipeline (Python)

## 📌 Project Overview
This project implements an end-to-end ETL (Extract, Transform, Load) pipeline using Python.
The pipeline fetches data from external REST APIs, transforms raw JSON into analytics-ready
tables, and loads the processed data into a relational database for reporting and analysis.

This project simulates a real-world data engineering workflow commonly used in analytics
and business intelligence environments.

## 🛠 Tech Stack
- Python
- Pandas
- Requests
- SQLite
- SQL
- Git & GitHub

## 🔄 ETL Workflow

### 1️⃣ Extract
- Data is retrieved from public REST APIs
- Endpoints used:
  - Users API
  - Posts API
- Retry logic and timeouts implemented for reliability

### 2️⃣ Transform
- JSON data normalized into tabular format
- Data cleaning and validation applied
- Dimension and fact tables created
- Aggregated KPIs generated

### 3️⃣ Load
- Transformed data loaded into SQLite database
- Tables created:
  - `dim_users`
  - `fact_posts`
  - `user_post_summary`
    
## 🛠 Tools & Technologies (Conceptual)
- **Python** → ETL logic implementation
- **REST APIs** → Data source
- **Pandas** → Data transformation
- **SQLite** → Relational storage
- **GitHub** → Version control and collaboration

## 🎯 Key Learning Outcomes
- Understanding end-to-end ETL workflows
- Designing scalable ETL architectures
- Working with API-based data sources
- Preparing data for analytics and reporting
- Applying data engineering best practices
