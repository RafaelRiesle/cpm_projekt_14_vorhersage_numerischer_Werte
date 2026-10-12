import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

from vnw.defines.defines import DATA_QUERY_FILE, QUERY_DATA_FILE

load_dotenv()

DB_SERVER = os.getenv("DB_SERVER")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


class SqlServerConnector:
    def __init__(self) -> None:
        if not all([DB_SERVER, DB_NAME, DB_USER, DB_PASSWORD]):
            raise ValueError("Fehlende Datenbank-Konfiguration in der .env Datei!")

        self.connection_string = (
            f"mssql+pymssql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"
        )
        self.engine = None
        self.export_file = QUERY_DATA_FILE
        self.query_path = DATA_QUERY_FILE

    def connect(self) -> None:
        try:
            self.engine = create_engine(self.connection_string)
            print("Verbindung erfolgreich hergestellt!")
        except Exception as e:
            print("Verbindungsfehler:", e)

    def query_dataframe(self, query: str) -> pd.DataFrame:
        if not self.engine:
            raise Exception("Nicht verbunden. Bitte zuerst .connect() aufrufen.")

        with self.engine.connect() as conn:
            return pd.read_sql_query(query, conn)

    def get_sql_query(self) -> str:
        with open(self.query_path, encoding="utf-8") as f:
            return f.read()

    def save_as_parquet(self, df: pd.DataFrame, file_path: Path) -> None:
        file_path = Path(file_path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(file_path)

    def close(self) -> None:
        if self.engine:
            self.engine.dispose()
        print("Verbindung geschlossen.")

    def get_data(self) -> None:
        self.connect()

        df = self.query_dataframe(self.get_sql_query())
        self.save_as_parquet(df, self.export_file)

        self.close()
