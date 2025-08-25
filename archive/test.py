import pandas as pd

from plotting import create_lineplot

df = pd.read_csv("processed_microplastics.csv")

fruits_trend = df.groupby("year")["fruits"].median().reset_index()

create_lineplot(
    fruits_trend,
    "year",
    "fruits",
    "Global Average Microplastic Content in Fruits (1990–2018)",
)
