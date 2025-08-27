import pandas as pd
import streamlit as st
from src.model import validate_data
import io

def main():
    st.title("CSV Data Validator")
    st.write("Upload a CSV file to validate its contents against the defined schema.")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Data Preview:")
        st.dataframe(df)

        # Botão para baixar todos os dados em JSON
        

        if st.button("Validate"):
            validation_results = validate_data(df)
            st.write("Validation Results:")

            errors = [r for r in validation_results if "Erro" in r]
            warnings = [r for r in validation_results if "Warning" in r]
            oks = [r for r in validation_results if "OK" in r]

            st.write(f"Erros: {len(errors)}")
            st.write(f"Warnings: {len(warnings)}")
            st.write(f"OK: {len(oks)}")
            for result in errors:
                st.error(result)
            # for result in warnings:
            #     st.warning(result)
            # for result in oks:
            #     st.success(result)

            if len(errors) == 0:
                st.success("All rows are valid!")
                json_data = df.to_json(orient="records", force_ascii=False, indent=2)
                st.download_button(
                    label="Download todos os dados em JSON",
                    data=json_data,
                    file_name="data.json",
                    mime="application/json"
                )
                st.balloons()

           

if __name__ == "__main__":
    main()