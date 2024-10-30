# Databricks notebook source
# MAGIC %pip install kagglehub

# COMMAND ----------

df_loans = spark.read.csv(path, header=True, inferSchema=True)

# COMMAND ----------

df_loans.display()

# COMMAND ----------

df_spark = spark.createDataFrame(df_loans)
df_spark.write.saveAsTable("dev.loan_prediction_test.bankloan")
