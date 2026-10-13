import pandas as pd


def calculate_amount_per_column(
    df: pd.DataFrame, group_column: str, sum_column: str
) -> pd.DataFrame:
    return (
        df.groupby(group_column)[sum_column]
        .sum()
        .reset_index(name=f"Sum{sum_column}")
        .sort_values(ascending=False, by=f"Sum{sum_column}")
        .round(2)
    )
