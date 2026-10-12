from pathlib import Path

BASE_FOLDER_PATH = Path(__file__).resolve().parents[3]

RAW_DATA_FOLDER_PATH = BASE_FOLDER_PATH / "data/raw"
QUERY_DATA_FILE = RAW_DATA_FOLDER_PATH / "sql_results.parquet"

DATA_QUERY_FOLDER = BASE_FOLDER_PATH / "queries"
DATA_QUERY_FILE = DATA_QUERY_FOLDER / "data_query.sql"
