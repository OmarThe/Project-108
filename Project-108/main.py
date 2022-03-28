import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("data.csv")
data_list = df["Avg Rating"].to_list()

fig = ff.create_distplot([data_list],["Avg Rating"])
fig.show()
