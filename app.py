import pandas as pd
import streamlit as st
from src.model import validate_data


def main():
    st.title("CSV Data Validator")
    st.write("Upload a CSV file to validate its contents against the defined schema.")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Data Preview:")
        st.dataframe(df)

        validation_results = validate_data(df)
        st.write("Validation Results:")
        for result in validation_results:
            st.write(result)

if __name__ == "__main__":
    main()