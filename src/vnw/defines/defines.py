from pathlib import Path

BASE_FOLDER_PATH = Path(__file__).resolve().parents[3]

DATA_FOLDER_PATH = BASE_FOLDER_PATH / "data"

RAW_DATA_FOLDER_PATH = DATA_FOLDER_PATH / "raw"
QUERY_DATA_FILE = RAW_DATA_FOLDER_PATH / "sql_results.parquet"

TRAINSET_PATH = DATA_FOLDER_PATH / "trainset.parquet"
VALSET_PATH = DATA_FOLDER_PATH / "valset.parquet"
TESTSET_PATH = DATA_FOLDER_PATH / "testset.parquet"

DATA_QUERY_FOLDER = BASE_FOLDER_PATH / "queries"
DATA_QUERY_FILE = DATA_QUERY_FOLDER / "data_query.sql"
