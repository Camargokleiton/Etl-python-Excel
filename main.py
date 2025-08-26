# import sweetviz as sv
# import pandas as pd

# df = pd.read_csv("data.csv")
# report = sv.analyze(df)
# report.show_html("sweetviz_report.html")

from great_expectations.dataset import PandasDataset
import pandas as pd

df = pd.read_csv("data.csv")
dataset = PandasDataset(df)

# Exemplo de validação
print(dataset.expect_column_values_to_not_be_null("Organizador"))
