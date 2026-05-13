from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
import os
import sys
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

# Définition du schéma correspondant aux données de l'API Crypto
schema = StructType([
    StructField("tr_id", StringType(), True),      # ID unique de la transaction
    StructField("user_id", StringType(), True),    # "market_api"
    StructField("amount", DoubleType(), True),     # Le prix de la crypto (Nombre décimal)
    StructField("currency", StringType(), True),   # "USD"
    StructField("merchant", StringType(), True),   # Nom de la crypto (ex: Bitcoin)
    StructField("timestamp", StringType(), True)   # Date et heure de l'appel API
])

# On pointe vers le dossier que tu as montré sur ta photo
os.environ['HADOOP_HOME'] = "C:/hadoop"
os.environ['PATH'] += os.pathsep + "C:/hadoop/bin"

# Configuration de la session Spark avec les connecteurs Kafka
spark = SparkSession.builder \
    .appName("FintechIngestionBronze") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0") \
    .getOrCreate()


# 1. Lecture du flux (ici on l'appelle df_raw)
df_raw = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "transactions_raw") \
    .option("startingOffsets", "earliest") \
    .load()

# 2. Transformation (on utilise le MÊME nom que celui du dessus)
df_json = df_raw.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Transformation du format binaire Kafka en colonnes lisibles
df_json = df_raw.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Écriture dans le Data Lake (Couche Bronze) au format Parquet
query = df_json.writeStream \
    .format("parquet") \
    .option("path", "data/bronze") \
    .option("checkpointLocation", "data/checkpoints") \
    .outputMode("append") \
    .start()


print("📥 Ingestion en cours vers la couche Bronze...")
query.awaitTermination()