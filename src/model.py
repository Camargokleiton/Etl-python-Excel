import pandas as pd
from validator import DataFrameValidator
import streamlit as st

def validate_data(file):
    df = pd.read_csv(file)
    
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

if __name__ == "__main__":
    st.title("CSV Data Validator")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        validation_results = validate_data(uploaded_file)
        for result in validation_results:
            st.write(result)