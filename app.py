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

        if st.button("Show Data Summary"):
            st.write("Data Summary:")
            st.write(df.describe(include='all'))
        if st.button("Validate"):
            validation_results = validate_data(df)
            st.write("Validation Results:")

            errors = [r for r in validation_results if "Erro" in r]
            warnings = [r for r in validation_results if "Warning" in r]
            oks = [r for r in validation_results if "OK" in r]

            

            for result in errors:
                st.error(result)
            # for result in warnings:
            #     st.warning(result)
            # for result in oks:
            #     st.success(result)

            
            if st.button("Salvar apenas linhas validadas (OK)"):
                ok_indices = [int(r.split()[1]) for r in oks]
                df_ok = df.iloc[ok_indices]
                output = io.BytesIO()
                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                    df_ok.to_excel(writer, index=False)
                output.seek(0)
                st.download_button(
                    label="Download planilha validada",
                    data=output.getvalue(),
                    file_name="dados_validados.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

if __name__ == "__main__":
    main()