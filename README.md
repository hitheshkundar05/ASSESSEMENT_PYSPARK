# Air Quality Data Analysis using PySpark on Databricks

## Project Overview

This project demonstrates a complete PySpark data engineering workflow using Databricks. The project uses an Air Quality dataset from Kaggle to perform data ingestion, exploration, cleaning, transformations, SQL analysis, and storage of processed data.

---

# Dataset Description

* **Dataset Name:** Air Quality Data in India (Extended)
* **File Used:** /Volumes/workspace/default/data_vol/station_hour_transformed.csv
* **Source:** Kaggle
* **Dataset URL:** https://www.kaggle.com/datasets/neomatrix369/air-quality-data-in-india-extended

The dataset contains hourly air quality measurements collected from monitoring stations across India. It includes pollutant concentrations such as PM2.5, PM10, NO₂, SO₂, CO, O₃, Air Quality Index (AQI), city, state, station details, season, month, and AQI category.

---

# Technologies Used

* Apache Spark (PySpark)
* Databricks
* Python
* Spark SQL

---

# Project Steps

## 1. Dataset Upload

* Downloaded the dataset from Kaggle.
* Uploaded `station_hour_transformed.csv` to the Databricks Unity Catalog Volume.

---

## 2. Reading the Dataset

The dataset was read using three different Spark read modes:

* **PERMISSIVE** – Reads all records and stores malformed records instead of failing.
* **DROPMALFORMED** – Ignores malformed records.
* **FAILFAST** – Stops reading immediately if any malformed record is found.

Finally, the dataset was processed using the appropriate read mode.

---

## 3. Data Exploration

Performed the following exploratory operations:

* Printed all column names.
* Counted the total number of rows.
* Displayed the DataFrame schema.
* Counted the total number of columns.
* Displayed the first five records.

---

## 4. Corrupted Record Detection

Checked whether the `_corrupt_record` column exists.

No corrupted records were found in the dataset.

---

## 5. Schema Validation

Validated the inferred schema and converted the **AQI** column to the **Double** data type using the `cast()` function for numerical analysis.

---

## 6. Data Transformations

The following transformations were applied:

* Renamed **StationName** to **Station_Name**.
* Removed the unnecessary **Unnamed: 0** column.
* Filtered records where **AQI > 200**.
* Created a new **Pollution_Level** column using conditional logic.
* Removed duplicate records using `dropDuplicates()`.
* Filled missing values in **City**, **State**, and **AQI_Bucket**.

---

## 7. Null Value Handling

Missing values were replaced with meaningful values:

* City → Unknown
* State → Unknown
* AQI_Bucket → Unknown

This approach preserved records instead of deleting them.

---

## 8. Duplicate Removal

Duplicate records were removed using the `dropDuplicates()` function to improve data quality.

---

## 9. Saving Processed Data

The cleaned dataset was saved as:

* Databricks Table: `AQI_Clean`
* Parquet format in Unity Catalog Volume

---

# Screenshots Included

Include screenshots of the following outputs

* Schema 
* Column update
* Drop null values

---

# Justification for Decisions

### Read Mode

The dataset was tested with **PERMISSIVE**, **DROPMALFORMED**, and **FAILFAST** modes to understand Spark's handling of malformed records. **PERMISSIVE** was chosen because it allows processing to continue while preserving malformed records for inspection.

### Transformations

The transformations improved the dataset by:

* Renaming columns for better readability.
* Removing unnecessary columns.
* Filtering highly polluted records (AQI > 200).
* Creating a pollution category.
* Eliminating duplicate records.

### Null Handling Strategy

Instead of deleting rows containing null values, missing values were replaced with meaningful defaults such as **Unknown**, ensuring that useful records were retained.

---

# Challenges Faced

### Challenge 1

Handling columns containing special characters (for example, `PM2.5`).

**Solution**

Referenced the column correctly or renamed it before processing.

---

### Challenge 2

Incorrect data types after loading the CSV.

**Solution**

Used the `cast()` function to convert the AQI column to `DoubleType`.

---

### Challenge 3

Understanding different Spark read modes.

**Solution**

Tested PERMISSIVE, DROPMALFORMED, and FAILFAST modes and compared their behaviour.

---

### Challenge 4

Working with Databricks Unity Catalog and Spark SQL tables.

**Solution**

Successfully stored the processed dataset as both a managed table and a Parquet file.

---

# Conclusion

This project demonstrates the complete data engineering pipeline using PySpark on Databricks, including dataset ingestion, exploration, schema validation, data transformation, null value handling, duplicate removal, SQL analysis, and efficient storage using Spark tables and Parquet format.
