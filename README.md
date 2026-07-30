# ASSESSEMENT_PYSPARK
# Air Quality Data Analysis using PySpark on Databricks

## Project Overview

This project demonstrates data engineering concepts using **Apache Spark (PySpark)** on **Databricks**. The objective is to perform data ingestion, data exploration, schema validation, data cleaning, transformations, null value handling, duplicate removal, and save the processed data in an efficient format.

---

## Dataset Information

* **Dataset Name:** Station Hour Transformed (Air Quality Dataset)
* **Source:** Kaggle
* **Dataset File:** `station_hour_transformed.csv`
* **Domain:** Air Quality Monitoring

The dataset contains hourly air quality measurements collected from different monitoring stations. It includes pollutant concentrations, Air Quality Index (AQI), city, state, station information, season, month, and other environmental attributes.

---

## Technologies Used

* Apache Spark (PySpark)
* Databricks
* Python
* SQL

---

## Project Workflow

### 1. Dataset Upload

* Downloaded the dataset from Kaggle.
* Uploaded the CSV file into Databricks Catalog.

### 2. Reading the Dataset

* Loaded the dataset into a Spark DataFrame.
* Used **PERMISSIVE** mode with header and schema inference.

### 3. Data Exploration

Performed the following exploratory tasks:

* Printed all column names.
* Counted the total number of rows.
* Displayed the schema.
* Counted the total number of columns.
* Displayed sample records.

### 4. Corrupted Record Detection

* Checked whether the `_corrupt_record` column exists.
* Verified that the dataset contains no corrupted records.

### 5. Schema Validation

* Verified the inferred schema.
* Converted required columns to appropriate data types using `cast()`.

### 6. Data Transformations

The following transformations were performed:

* Renamed columns using `withColumnRenamed()`.
* Filtered records with AQI greater than 200.
* Added a constant column (`Country = India`) using `lit()`.
* Created new columns using `withColumn()`.
* Cast columns to appropriate numeric types.
* Dropped unnecessary columns.
* Used aliases for better readability.

### 7. Null Value Handling

* Identified null values in every column.
* Filled missing values with meaningful defaults where appropriate.

### 8. Duplicate Removal

* Removed duplicate records using `dropDuplicates()`.

### 9. Saving Processed Data

* Saved the cleaned DataFrame as a Parquet file.
* Saved the processed dataset as a Databricks table.

---

## SQL Analysis

The following SQL queries were executed:

1. Top 10 cities with the highest average AQI.
2. Number of monitoring stations in each state.
3. Count of records in each AQI category.
4. Average PM2.5 concentration by season.

---

## Screenshots Included

The repository contains screenshots of:

* Dataset upload
* DataFrame schema
* DataFrame preview
* Row count
* Column count
* Null value analysis
* Data transformations
* SQL query outputs
* Final saved table

---

## Challenges Faced

* Handling columns with special characters such as `PM2.5`.
* Converting incorrect data types using `cast()`.
* Understanding Spark DataFrame transformations.
* Working with Databricks Catalog and SQL tables.

---

## Conclusion

This project demonstrates the complete PySpark data engineering workflow, including loading data, validating schema, cleaning data, applying transformations, handling null values, performing SQL analysis, and storing the processed dataset using Databricks.

