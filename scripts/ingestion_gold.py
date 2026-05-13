from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max, min
import os

# Config Windows
os.environ['HADOOP_HOME'] = "C:/hadoop"
os.environ['PATH'] += os.pathsep + "C:/hadoop/bin"

spark = SparkSession.builder.appName("FintechGold").getOrCreate()

# 1. Lire la couche Silver
df_silver = spark.read.parquet("data/silver")

# 2. Agrégation (C'est ça le Data Warehouse / Gold)
df_gold = df_silver.groupBy("merchant").agg(
    avg("amount_mad").alias("prix_moyen_mad"),
    max("amount_mad").alias("prix_max_mad"),
    min("amount_mad").alias("prix_min_mad")
)

# 3. Écrire dans Gold
df_gold.write \
    .mode("overwrite") \
    .parquet("data/gold")

print("🏆 Couche GOLD (Data Warehouse) générée avec succès !")
df_gold.show()
spark.stop()