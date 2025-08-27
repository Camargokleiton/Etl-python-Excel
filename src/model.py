import pandas as pd
from src.validator import DataFrameValidator


def validate_data(df):

    df = df.copy()

    df.columns = (
        df.columns
        .str.normalize("NFKD")
        .str.encode("ascii", errors="ignore")  
        .str.decode("utf-8")
        .str.replace(" ", "_")
    )

    results = []
    for idx, row in df.iterrows():
        try:
            record = DataFrameValidator(**row.to_dict())
            results.append(f"Linha {idx} OK: {record}")
        except Exception as e:
            results.append(f"Erro na linha {idx}: {e}")
    
    return results

