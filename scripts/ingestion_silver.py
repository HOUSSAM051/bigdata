from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when
import os

# Configuration Hadoop pour Windows
os.environ['HADOOP_HOME'] = "C:/hadoop"
os.environ['PATH'] += os.pathsep + "C:/hadoop/bin"

spark = SparkSession.builder \
    .appName("FintechIngestionSilver") \
    .getOrCreate()

print("🥈 Lecture de la couche Bronze...")

# 1. Lecture des données brutes (Parquet)

df_bronze = spark.read.parquet("data/bronze")

# 2. Nettoyage et Transformation (ETL)
df_silver = df_bronze \
    .dropDuplicates(["tr_id"]) \
    .filter(col("amount").isNotNull()) \
    .withColumn("amount_mad", col("amount") * 10.0) \
    .withColumn("priority", when(col("amount") > 1000, "HIGH").otherwise("NORMAL"))

print("✨ Transformation terminée. Écriture vers la couche Silver...")

# 3. Écriture vers la couche Silver
df_silver.write \
    .mode("overwrite") \
    .parquet("data/silver")

print("✅ Couche Silver mise à jour avec succès !")
spark.stop()
