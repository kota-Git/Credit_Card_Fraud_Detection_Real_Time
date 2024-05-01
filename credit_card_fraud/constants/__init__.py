import os
from datetime import date

DATABASE_NAME="credit_card_DB"

COLLECTION_NAME="fraud_data"

MONGODB_URL_KEY="MONGODB_URL"

PIPELINE_NAME:str ="credit_card_fraud"

ARTIFICAT_DIR:str="artificat"

MODEL_FILE_NAME="model.pkl"

TARGET_COLUMN="default payment next month"

PREPROCESSING_OBJECT_FILE_NAME="preprocessing.pkl"


FILE_NAME:str="default of credit card data.xls"

TRAIN_FILE_NAME:str="train.xls"

TEST_FILE_NAME:str="test.xls"


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "fraud_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2