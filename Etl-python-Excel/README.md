# Etl-python-Excel Project

## Overview
This project is designed to read and validate data from a CSV file named `data.csv`. It utilizes the Pandas library for data manipulation and Pydantic for data validation. Additionally, a Streamlit application is provided to facilitate user interaction through file uploads.

## Project Structure
```
Etl-python-Excel
├── src
│   ├── model.py         # Contains logic to read and validate CSV data
│   └── validator.py     # Defines the data validation schema using Pydantic
├── app.py               # Entry point for the Streamlit application
├── data.csv             # CSV file containing the data to be validated
└── README.md            # Documentation for the project
```

## Requirements
To run this project, you need to have the following Python packages installed:
- pandas
- pydantic
- streamlit

You can install the required packages using pip:
```
pip install pandas pydantic streamlit
```

## Usage
1. Place your `data.csv` file in the project root directory.
2. Run the Streamlit application by executing the following command in your terminal:
   ```
   streamlit run app.py
   ```
3. Open the provided URL in your web browser.
4. Use the file upload feature to select and upload your `data.csv` file.
5. The application will validate the contents of the uploaded file and display the results.

## Validation
The data in `data.csv` will be validated against the following schema defined in `validator.py`:
- **Organizador**: int
- **Ano_Mes**: str
- **Dia_da_Semana**: str
- **Tipo_Dia**: str
- **Objetivo**: str
- **Date**: str (format: dd/mm/yyyy)
- **AdSet_name**: str
- **Amount_spent**: float
- **Link_clicks**: Optional[int]
- **Impressions**: Optional[int]
- **Conversions**: Optional[float]
- **Segmentacao**: str
- **Tipo_de_Anuncio**: str
- **Fase**: str

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.