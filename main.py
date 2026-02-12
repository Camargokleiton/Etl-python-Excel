import sweetviz as sv
import pandas as pd
from great_expectations.dataset import PandasDataset
from dataprofiler import Profiler

df = pd.read_csv("data.csv") #Data frame
df25 = pd.read_csv("data_2025.csv") #Data frame

report = sv.analyze(df)
report25 = sv.analyze(df25)
report25.show_html("dataReport.html")


dataset = PandasDataset(df)


profile = Profiler(df)


# report = profile.report()
# print(report)
