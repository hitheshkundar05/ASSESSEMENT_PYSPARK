# Databricks notebook source
spark

# COMMAND ----------

from pyspark.sql.functions import col

# COMMAND ----------

df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("mode", "PERMISSIVE") \
    .csv("/Volumes/workspace/default/data_vol/station_hour_transformed.csv")
df.display()

# COMMAND ----------

df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("mode", "DROPMALFORMED") \
    .csv("/Volumes/workspace/default/data_vol/station_hour_transformed.csv")
df.display()

# COMMAND ----------

df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("mode", "FAILFAST") \
    .csv("/Volumes/workspace/default/data_vol/station_hour_transformed.csv")
df.display()

# COMMAND ----------

# Column names
print(df.columns)

# Total rows
print(df.count())

# Schema
df.printSchema()

# Number of columns
print(len(df.columns))

# Preview
df.show(5)

# COMMAND ----------

if "_corrupt_record" in df.columns:
    df.filter("_corrupt_record IS NOT NULL").show()
else:
    print("No corrupted records found.")

# COMMAND ----------

df = df.withColumn("AQI", col("AQI").cast("double"))

# COMMAND ----------

df = df.withColumnRenamed("StationName","Station_Name")

# COMMAND ----------

df = df.drop("Unnamed: 0")

# COMMAND ----------

df_clean = spark.table("AQI_Clean")
df_high = df_clean.filter(df_clean.AQI > 200)
df_high.limit(5).display()

# COMMAND ----------

from pyspark.sql.functions import when

df = df.withColumn(
    "Pollution_Level",
    when(df.AQI <= 50,"Good")
    .when(df.AQI <=100,"Moderate")
    .when(df.AQI <=200,"Poor")
    .otherwise("Severe")
)
df_high.limit(5).display()

# COMMAND ----------

df = df.dropDuplicates()

# COMMAND ----------

df = df.fillna({
    "City":"Unknown",
    "State":"Unknown",
    "AQI_Bucket":"Unknown"
})

# COMMAND ----------

df = df.dropDuplicates()

# COMMAND ----------

df.write.mode("overwrite").saveAsTable("AQI_Clean")

# COMMAND ----------

df.write.mode("overwrite").parquet("/Volumes/workspace/default/data_vol/station_hour_transformed")

# COMMAND ----------

# MAGIC %md
# MAGIC Top 10 Most Polluted Cities

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT City,
# MAGIC AVG(AQI) AS Average_AQI
# MAGIC FROM AQI_Clean
# MAGIC GROUP BY City
# MAGIC ORDER BY Average_AQI DESC
# MAGIC LIMIT 5;

# COMMAND ----------

# MAGIC %md
# MAGIC Number of Stations in Each State

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT State,
# MAGIC COUNT(DISTINCT StationId) AS Stations
# MAGIC FROM AQI_Clean
# MAGIC GROUP BY State
# MAGIC ORDER BY Stations DESC;

# COMMAND ----------

# MAGIC %md
# MAGIC AQI Category Count

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT AQI_Bucket,
# MAGIC COUNT(*) AS Total
# MAGIC FROM AQI_Clean
# MAGIC GROUP BY AQI_Bucket
# MAGIC ORDER BY Total DESC;